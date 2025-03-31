import asyncio
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
from io import BytesIO
from pytube import YouTube
import instaloader
import requests

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Конфигурация
CHANNEL_ID = "-1002101328852"  # Замените на username вашего канала
ADMIN_IDS = [1203146294]  # Замените на ID админов
TOKEN = "7560363659:AAHxj3sNLAV3P2FfnD3Js9-cNnxNSs1T6HU"  # Замените на токен вашего бота
TIKTOK_API_KEY = "your_tiktok_api_key"  # Замените на ваш API-ключ для TikTok
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 МБ (ограничение Telegram)
SEND_TIMEOUT = 30  # Тайм-аут отправки в секундах

# Статистика
stats = {
    "users": set(),
    "downloads": {"youtube": 0, "tiktok": 0, "instagram": 0, "twitch": 0, "vk": 0, "pinterest": 0}
}


# Проверка подписки
async def is_subscribed(user_id: int, bot):
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        logger.error(f"Ошибка проверки подписки: {e}")
        return False


# Команда /start
async def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    stats["users"].add(user_id)
    if await is_subscribed(user_id, context.bot):
        await update.message.reply_text("Привет! Ты подписан на канал. Используй /download для скачивания видео.")
    else:
        await update.message.reply_text("Привет! Подпишись на канал, чтобы использовать бота.")


# Скачивание видео с YouTube
async def download_youtube(url: str):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    buffer = BytesIO()
    video.stream_to_buffer(buffer)
    buffer.seek(0)
    return buffer, video.filesize


# Скачивание видео с Instagram
async def download_instagram(url: str):
    L = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
    response = requests.get(post.video_url, stream=True, timeout=10)
    buffer = BytesIO()
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            buffer.write(chunk)
    buffer.seek(0)
    return buffer, buffer.getbuffer().nbytes


# Скачивание видео с TikTok
async def download_tiktok(url: str):
    response = requests.get(f"https://api.tiktok.com/download?url={url}&apikey={TIKTOK_API_KEY}", timeout=10)
    video_url = response.json()['video_url']
    video_response = requests.get(video_url, stream=True, timeout=10)
    buffer = BytesIO()
    for chunk in video_response.iter_content(chunk_size=8192):
        if chunk:
            buffer.write(chunk)
    buffer.seek(0)
    return buffer, buffer.getbuffer().nbytes


# Визуализация загрузки
async def show_loading(update: Update):
    msg = await update.message.reply_text("⏳ Скачивание видео...")
    for text in ["⏳ Обработка видео...", "⏳ Подготовка к отправке..."]:
        await asyncio.sleep(2)
        await msg.edit_text(text)
    return msg


# Команда /download
async def download(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if not await is_subscribed(user_id, context.bot):
        return await update.message.reply_text("❌ Подпишитесь на канал для использования бота")

    if not context.args:
        return await update.message.reply_text("❌ Формат: /download <ссылка>")

    url = context.args[0]
    loading_msg = await show_loading(update)

    try:
        platform_handlers = {
            "youtube": (download_youtube, "youtube"),
            "instagram": (download_instagram, "instagram"),
            "tiktok": (download_tiktok, "tiktok")
        }

        for key in platform_handlers:
            if key in url:
                handler, platform = platform_handlers[key]
                buffer, size = await handler(url)
                break
        else:
            return await loading_msg.edit_text("❌ Платформа не поддерживается")

        if size > MAX_FILE_SIZE:
            await loading_msg.edit_text(f"❌ Файл слишком большой ({size // 1024 // 1024} МБ > 50 МБ)")
            return buffer.close()

        await loading_msg.edit_text("⏳ Отправка видео...")
        try:
            await asyncio.wait_for(
                update.message.reply_video(
                    video=InputFile(buffer, filename="video.mp4"),
                    caption="Ваше видео готово!",
                    supports_streaming=True
                ),
                timeout=SEND_TIMEOUT
            )
            stats["downloads"][platform] += 1
            await loading_msg.edit_text("✅ Видео успешно отправлено!")
        except asyncio.TimeoutError:
            await loading_msg.edit_text("❌ Тайм-аут отправки видео. Попробуйте позже")
        finally:
            buffer.close()

    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        await loading_msg.edit_text("❌ Ошибка при обработке видео")
        await update.message.reply_text(f"⚠️ Ошибка: {str(e)}")


# Команда /stats (только для админов)
async def stats_command(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id not in ADMIN_IDS:
        return await update.message.reply_text("❌ У вас нет доступа к этой команде")

    stats_text = (
        f"Пользователи: {len(stats['users'])}\n"
        f"Скачивания:\n"
        f"  YouTube: {stats['downloads']['youtube']}\n"
        f"  TikTok: {stats['downloads']['tiktok']}\n"
        f"  Instagram: {stats['downloads']['instagram']}\n"
        f"  Twitch: {stats['downloads']['twitch']}\n"
        f"  VK: {stats['downloads']['vk']}\n"
        f"  Pinterest: {stats['downloads']['pinterest']}"
    )
    await update.message.reply_text(stats_text)


# Команда /broadcast (рассылка, только для админов)
async def broadcast(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id not in ADMIN_IDS:
        return await update.message.reply_text("❌ У вас нет доступа к этой команде")

    if not context.args:
        return await update.message.reply_text("❌ Формат: /broadcast <сообщение>")

    message = " ".join(context.args)
    for user in stats["users"]:
        try:
            await context.bot.send_message(chat_id=user, text=message)
        except Exception as e:
            logger.error(f"Ошибка отправки сообщения пользователю {user}: {e}")


# Обработка ошибок
async def error(update: Update, context: CallbackContext):
    logger.error(f"Ошибка: {context.error}")


# Основная функция
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handlers([
        CommandHandler("start", start),
        CommandHandler("download", download),
        CommandHandler("stats", stats_command),
        CommandHandler("broadcast", broadcast)
    ])
    application.add_error_handler(error)
    application.run_polling()


if __name__ == '__main__':
    main()



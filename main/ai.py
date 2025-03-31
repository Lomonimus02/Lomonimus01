import random


class Player:
    def __init__(self, name):
        self.health = 4
        self.name = name
        self.items = []


def take_turn(player, opponent, chambers):
    while True:
        if player.items:
            use_item = input(f"{player.name}, вы хотите использовать предмет? (Да/Нет): ").lower()
            if use_item == 'да':
                use_item_action(player, opponent, chambers)
                continue

        action = input(f"{player.name}, выстрелить в себя (1) или в {opponent.name} (2)? ")
        if action == '1':
            if not chambers:
                chambers.extend(setup_game())
            chamber = chambers.pop(0)
            if chamber == 'bullet':
                player.health -= 1
                print(f"Бах! {player.name} получил урон. У него осталось {player.health} здоровья.")
                return
            else:
                print(f"Щелчок! {player.name} продолжает.")
        elif action == '2':
            if not chambers:
                chambers.extend(setup_game())
            chamber = chambers.pop(0)
            if chamber == 'bullet':
                opponent.health -= 1
                print(f"Бах! {opponent.name} получил урон. У него осталось {opponent.health} здоровья.")
            else:
                print(f"Щелчок! {opponent.name} не получил урон.")
            return
        else:
            print("Неверный выбор. Попробуйте снова.")


def computer_turn(player, opponent, chambers):
    if player.items:
        use_item_action(player, opponent, chambers)
        return computer_turn(player, opponent, chambers)

    action = random.choice(['1', '2'])
    if action == '1':
        print(f"{player.name} решает выстрелить в себя.")
        if not chambers:
            chambers.extend(setup_game())
        chamber = chambers.pop(0)
        if chamber == 'bullet':
            player.health -= 1
            print(f"Бах! {player.name} получил урон. У него осталось {player.health} здоровья.")
        else:
            print(f"Щелчок! {player.name} продолжает.")
            return computer_turn(player, opponent, chambers)
    elif action == '2':
        print(f"{player.name} решает выстрелить в {opponent.name}.")
        if not chambers:
            chambers.extend(setup_game())
        chamber = chambers.pop(0)
        if chamber == 'bullet':
            opponent.health -= 1
            print(f"Бах! {opponent.name} получил урон. У него осталось {opponent.health} здоровья.")
        else:
            print(f"Щелчок! {opponent.name} не получил урон.")
    return


def setup_game():
    total_chambers = random.randint(3, 8)
    num_bullets = random.randint(1, total_chambers - 1)  # Один пустой патрон всегда остается
    chambers = ['bullet'] * num_bullets + ['empty'] * (total_chambers - num_bullets)
    random.shuffle(chambers)
    print(f"Перед началом игры:\nЗаряженных патронов: {num_bullets}\nПустых патронов: {total_chambers - num_bullets}")
    return chambers


def distribute_items():
    items = ['Лупа', 'Пиво', 'Пила', 'Наручники', 'Сигареты']
    player_items = random.sample(items, 2)
    dealer_items = random.sample(items, 2)
    return player_items, dealer_items


def use_item_action(player, opponent, chambers):
    item = input(f"{player.name}, выберите предмет для использования: {player.items} ")
    if item == 'Лупа':
        print(f"{player.name} использовал Лупу.")
        if chambers:
            print(f"Следующая пуля: {'заряжена' if chambers[0] == 'bullet' else 'пустая'}.")
    elif item == 'Пиво':
        print(f"{player.name} использовал Пиво.")
        if chambers:
            removed_bullet = chambers.pop(0)
            print(f"Пуля была {'заряжена' if removed_bullet == 'bullet' else 'пустая'}.")
    elif item == 'Пила':
        print(f"{player.name} использовал Пилу. Урон удвоен на один ход.")
        player.damage_multiplier = 2
    elif item == 'Наручники':
        print(f"{player.name} использовал Наручники. {opponent.name} пропускает следующий ход.")
        opponent.skip_turn = True
    elif item == 'Сигареты':
        print(f"{player.name} использовал Сигареты. Восстановлено 1 здоровье.")
        player.health += 1

    player.items.remove(item)


def play_game():
    while True:
        player_name = input("Введите имя игрока: ")
        if player_name.lower() in ["god", "dealer", "бог"]:
            print("Это имя недоступно. Пожалуйста, выберите другое имя.")
        else:
            break

    player = Player(player_name)
    dealer = Player("Dealer")

    player.items, dealer.items = distribute_items()

    agreement = input("Согласны ли вы с условиями игры? (Да/Нет): ")
    if agreement.lower() != "да":
        print("Игра завершена.")
        return

    chambers = setup_game()

    print("Игра началась!")
    while player.health > 0 and dealer.health > 0:
        take_turn(player, dealer, chambers)
        if dealer.health <= 0:
            print("Dealer проиграл! Вы победили!")
            return
        if dealer.skip_turn:
            dealer.skip_turn = False
            print("Dealer пропустил ход.")
            continue
        computer_turn(dealer, player, chambers)
        if player.health <= 0:
            print("Вы проиграли! Dealer победил!")
            return


play_game()

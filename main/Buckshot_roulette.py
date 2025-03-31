from random import randint


HP = 4
HP_op = 4
turn = 0
d = []
if HP == 0:
    print("Вы проиграли!")
else:
    if HP_op == 0:
        print("Вы победили!")
    else:
        bullet_count = randint(3, 8)
        blank_bullet_count = randint(1, bullet_count-1)
        live_bullet_count = bullet_count - blank_bullet_count
        print("Заряженных патронов:", live_bullet_count, "Холостых патронов:", blank_bullet_count)
        while bullet_count != 0:
            if HP == 0:
                print("Вы проиграли!")
            else:
                if HP_op == 0:
                    print("Вы победили!")
                else:
                    if turn == 0:
                        print("Ваш ход")
                        print("Выберите в кого стрелять")
                        print("0-в себя 1-в оппонента")
                        who_shot = int(input())
                        if who_shot == 0:
                            what_bullet = 0

                        turn += 1
                    elif turn == 1:
                        turn -= 1


            bullet_count -= 1
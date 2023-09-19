for i in range(80):
    print()

print("Hello! Это игра pong. Она предназначена для одного или двух игроков. Правила таковы:")
print("Игрок чтобы выиграть должен получить 21 очко.")
print("Если один из игроков смог отбить мяч, то очки не зачисляются")
print("Но если один из игроков не поймал мяч, то очко зачисляется другому игроку")
print("Правила просты. Дерзайте и выигрывайте!")
print()

score_to_win = 5

keyboard = input("Отправьте любой символ для начала игры: ")
start_ball_x_pos, start_ball_y_pos = 39, 12
start_rocket_1 = start_rocket_2= 11
rocket_1, rocket_2 = start_rocket_1, start_rocket_2
ball_x, ball_y = start_ball_x_pos, start_ball_y_pos
rocket_1_coins = rocket_2_coins = 0
ball_direction_x = ball_direction_y = 1
is_playing = True

def finish(rocket_1_coins, rocket_2_coins):
    if rocket_1_coins == 21:
        print("Поздравляем, игрок 1! Вы выиграли")
        print("Игрок 2. Не отчаивайтесь. У вас всё обязательно получится!")
    elif rocket_2_coins == 21:
        print("Поздравляем, игрок 2! Вы выиграли")
        print("Игрок 1. Не отчаивайтесь. У вас всё обязательно получится!")


def check_ball_y_direction(ball_y,ball_direction_y):
    if ball_y == 0:
        ball_direction_y *= -1
    elif ball_y == 24:
        ball_direction_y *= -1

    return ball_direction_y


def check_ball_x_direction(ball_x, ball_y, ball_direction_x, rocket_1, rocket_2):
        if ball_x == 1 and (ball_y == rocket_1 or ball_y == rocket_1 + 1 or ball_y == rocket_1 + 2):
            ball_direction_x *= -1
        elif ball_x == 78 and (ball_y == rocket_2 or ball_y == rocket_2 + 1 or ball_y == rocket_2 + 2):
            ball_direction_x *= -1

        return ball_direction_x


def stadium(rocket_1, rocket_2, ball_x, ball_y):
        for i in range(25):
            for j in range(80):
                if  (i >= rocket_1 and i <= rocket_1 + 2) and j == 0:
                    print("|", end="")
                elif (i == rocket_2 or i == rocket_2 + 1 or i == rocket_2 + 2) and j == 79:
                    print("|", end="")
                elif i == ball_y and j == ball_x:
                    print("o", end="")
                else:
                    print(".", end="")
            print()


while is_playing:
    print(f"Player 1: {rocket_1_coins}, Player 2: {rocket_2_coins}")
    stadium(rocket_1, rocket_2, ball_x, ball_y)

    keyboard = input()

    if keyboard in "aA" and rocket_1 != 0:
        rocket_1 -= 1
    elif keyboard in "zZ" and rocket_1 != 24:
        rocket_1 += 1
    elif keyboard in "kK" and rocket_2 != 0:
        rocket_2 -= 1
    elif keyboard in "mM" and rocket_2 != 24:
        rocket_2 += 1
    elif keyboard == "":
        pass
    else:
        continue

    if ball_x == 0:
        ball_x = start_ball_x_pos
        ball_y = start_ball_y_pos
        rocket_2_coins += 1
    elif ball_x == 79:
        ball_x = start_ball_x_pos
        ball_y = start_ball_y_pos
        rocket_1_coins += 1

    ball_direction_x = check_ball_x_direction(ball_x, ball_y, ball_direction_x, rocket_1, rocket_2)
    ball_direction_y = check_ball_y_direction(ball_y, ball_direction_y)

    ball_y += ball_direction_y
    ball_x += ball_direction_x

    finish(rocket_1_coins, rocket_2_coins)

    if rocket_1_coins == score_to_win or rocket_2_coins == score_to_win:
        print("Если вы хотите закончить игру напишите n или N. Если хотите повторить нажмите Y или y.")

        final_question = input()
        if final_question in "yY":
            rocket_1, rocket_2 = start_rocket_1, start_rocket_2
            ball_x, ball_y = start_ball_x_pos, start_ball_y_pos
            rocket_1_coins = rocket_2_coins = 0
        else:
            is_playing = False
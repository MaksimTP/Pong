rocket_1_start_pos = rocket_2_start_pos = 11

ball_x_start_pos = 39
ball_y_start_pos = 12
ball_x_direction = ball_y_direction = 1

score_1 = score_2 =  0

SCORE_TO_WIN = 21
HEIGHT = 25
WIDTH = 80

rocket_1 = rocket_1_start_pos
rocket_2 = rocket_2_start_pos

ball_x = ball_x_start_pos
ball_y = ball_y_start_pos
def pole(rocket_1, rocket_2, ball_x, ball_y):
    for j in range(HEIGHT):
        for i in range(WIDTH):
            if j == 0 or j == 24:
                print('-', end='')
            elif i == 0 or i == 79:
                print('|', end='')
            else:
                if i == 3 and (j in [rocket_1, rocket_1 + 1, rocket_1 + 2]):
                    print('|', end='')
                elif i == 77 and (j in [rocket_2, rocket_2 + 1, rocket_2 + 2]):
                    print('|', end='')
                elif i == ball_x and j == ball_y:
                    print('o', end = '')
                else:
                    print(' ', end='')
        print()

def collide_y_walls(ball_y, ball_y_direction):
    return ball_y_direction * -1 if ball_y == 23 or ball_y == 1 else ball_y_direction

def collide_x(ball_x,ball_y,ball_x_direction,ball_y_direction,score_1,score_2):
    if ball_x == 1:
        ball_x = ball_x_start_pos
        ball_y = ball_y_start_pos
        ball_x_direction *= -1
        ball_y_direction *= -1
        score_2 += 1
    if ball_x == 78:
        score_1 += 1
        ball_x = ball_x_start_pos
        ball_y = ball_y_start_pos
        ball_x_direction *= -1
        ball_y_direction *= -1
    return [ball_x,ball_y,ball_x_direction,ball_y_direction,score_1,score_2]

def collide_rockets(ball_x, rocket_1, rocket_2, ball_y,ball_x_direction):
    if ball_x == 76 and (rocket_2 == ball_y or rocket_2 + 1 == ball_y or rocket_2 + 2 == ball_y):
        ball_x_direction *= -1
    if ball_x == 4 and (rocket_1 == ball_y or rocket_1 + 1 == ball_y or rocket_1 + 2 == ball_y):
        ball_x_direction *= -1
    return ball_x_direction

def process_button(button, rocket_1, rocket_2):
    if button in 'aA' and rocket_1 != 1:
        rocket_1 -= 1
    if button in 'zZ' and rocket_1 != 21:
        rocket_1 += 1
    if button in 'kK' and rocket_2 != 1:
        rocket_2 -= 1
    if button in 'mM' and rocket_2 != 21:
        rocket_2 += 1
    if button == 'q':
        rocket_1 = -1
    return [rocket_1, rocket_2]


while rocket_1 != -1:

    print(f'score: {score_1}:{score_2}')
    pole(rocket_1, rocket_2, ball_x, ball_y)
    button = input()
    rocket_1, rocket_2 = process_button(button, rocket_1, rocket_2)

    ball_x += ball_x_direction
    ball_y += ball_y_direction
    ball_y_direction = collide_y_walls(ball_y, ball_y_direction)

    ball_x, ball_y, ball_x_direction, ball_y_direction, score_1, score_2 = collide_x(ball_x,ball_y,ball_x_direction,ball_y_direction,score_1,score_2)

    ball_x_direction = collide_rockets(ball_x, rocket_1, rocket_2, ball_y,ball_x_direction)


    if score_1 == SCORE_TO_WIN or score_2 == SCORE_TO_WIN:
        print(f"Поздравляем игрока {'1' if score_1 == SCORE_TO_WIN else '2'}!!! Ваш счет {score_1}:{score_2}")
        break


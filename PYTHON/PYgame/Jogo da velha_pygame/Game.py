import pygame
import random
import main as m
import menu

pygame.init()

# GLOBAL
screen = m.screen
clock = m.clock
tick = m.tick

# GAME VARIABLES
global turn, matriz_table, score, game
turn = 1
matriz_table = [['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']]
score = [0, 0]
game = 'pxp'

# COLORS
global transparent, black, white, red, blue, gray
transparent = (0, 0, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (102, 99, 99)

# IMAGES
arrow_return = pygame.image.load('images/arrow.png')
again = pygame.image.load('images/again.png')
home = pygame.image.load('images/home.png')


def home_button():
    mouse = pygame.mouse.get_pos()
    if 560 <= mouse[0] <= 600 and 0 <= mouse[1] <= 40:
        home = pygame.image.load('images/home _selected.png')
    else:
        home = pygame.image.load('images/home.png')

    home = pygame.transform.scale(home, (40, 40))
    screen.blit(home, [560, 0])


def again_button():
    mouse = pygame.mouse.get_pos()
    if 270 <= mouse[0] <= 330 and 440 <= mouse[1] <= 500:
        again = pygame.image.load('images/again_selected.png')
    else:
        again = pygame.image.load('images/again.png')

    again = pygame.transform.scale(again, (60, 60))
    screen.blit(again, [270, 440])


def arrow_button():
    mouse = pygame.mouse.get_pos()
    if 0 <= mouse[0] <= 50 and 0 <= mouse[1] <= 40:
        arrow_return = pygame.image.load('images/arrow_selected.png')
    else:
        arrow_return = pygame.image.load('images/arrow.png')

    arrow_return = pygame.transform.scale(arrow_return, (50, 40))
    screen.blit(arrow_return, [0, 0])


# DRAW THE TABLE TO PLAY
def table():
    x = 150
    y = 150
    pygame.draw.rect(screen, white, pygame.Rect(x, y, 300, 300))

    # LINES
    for n in range(2):
        y += 100
        pygame.draw.line(screen, black, (x, y), (x*3, y), 6)

    x = 150
    y = 150
    for m in range(2):
        x += 100
        pygame.draw.line(screen, black, (x, y), (x, y * 3), 6)


# WINNER SCREEN
def winner():
    global matriz_table, turn, score, game

    # INCREASE SCORE
    if turn % 2 == 1:
        score[0] += 1
    else:
        score[1] += 1

    # RESET THE GAME
    turn = 1
    matriz_table = [['-', '-', '-'],
                    ['-', '-', '-'],
                    ['-', '-', '-']]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # RETURN BUTTON ACTION
                if 0 <= x <= 50 and 0 <= y <= 40:
                    screen.fill(black)
                    score[0] = 0
                    score[1] = 0
                    game = 'pxp'
                    menu.secondary_menu()

                # AGAIN BUTTON ACTION
                elif 270 <= x <= 330 and 440 <= y <= 500:
                    if game == 'pxp':
                        menu.pxp()
                    else:
                        menu.pxc()

                # HOME BUTTON ACTION
                elif 560 <= x <= 600 and 0 <= y <= 40:
                    screen.fill(black)
                    matriz_table = [['-', '-', '-'],
                                    ['-', '-', '-'],
                                    ['-', '-', '-']]
                    turn = 1
                    score[0] = 0
                    score[1] = 0
                    menu.main_menu()

        screen.fill(black)

        # TEXT "WINNER"
        font = menu.font
        winner_text = menu.text_format('Winner', font, 100, white)
        winner_rect = winner_text.get_rect()
        screen.blit(winner_text, (300 - (winner_rect[2] / 2), 80))

        # WHO IS THE WINNER?
        if turn % 2 == 1:
            # DRAW "X"
            pygame.draw.line(screen, white, (250, 270), (350, 370), 12)
            pygame.draw.line(screen, white, (350, 270), (250, 370), 12)
        else:
            # DRAW "O"
            pygame.draw.circle(screen, white, (300, 320), 60, 9)

        # DISPLAY BUTTONS
        again_button()
        arrow_button()
        home_button()

        pygame.display.flip()


def status_game():
    global matriz_table, turn

    # STALEMATE:
    place_marked = 0
    for i in range(3):
        for n in range(3):
            if matriz_table[i][n] == 'o' or matriz_table[i][n] == 'x':
                place_marked += 1

    # STALEMATE CONDITION
    if place_marked == 9:
        turn = 1
        matriz_table = [['-', '-', '-'],
                        ['-', '-', '-'],
                        ['-', '-', '-']]
        if game == 'pxp':
            menu.pxp()
        else:
            menu.pxc()

    # CONDITION TO WIN
    mark = turn_()
    if matriz_table[0][0] == mark and matriz_table[0][1] == mark and matriz_table[0][2] == mark:
        winner()

    if matriz_table[0][0] == mark and matriz_table[1][0] == mark and matriz_table[2][0] == mark:
        winner()

    if matriz_table[0][0] == mark and matriz_table[1][1] == mark and matriz_table[2][2] == mark:
        winner()

    if matriz_table[0][2] == mark and matriz_table[1][2] == mark and matriz_table[2][2] == mark:
        winner()

    if matriz_table[2][0] == mark and matriz_table[2][1] == mark and matriz_table[2][2] == mark:
        winner()

    if matriz_table[2][0] == mark and matriz_table[1][1] == mark and matriz_table[0][2] == mark:
        winner()

    if matriz_table[0][1] == mark and matriz_table[1][1] == mark and matriz_table[2][1] == mark:
        winner()

    if matriz_table[1][0] == mark and matriz_table[1][1] == mark and matriz_table[1][2] == mark:
        winner()


# CHECK IF THE CURRENT POSITION IS MARKED
def check(y, x):
    if matriz_table[y][x] == '-':
        return False
    return True


def draw(y, x):
    global turn

    # CHECK THE GAME STATUS
    status_game()

    # DRAW 'X' IN CURRENT POSITION
    if turn % 2 == 1:
        pygame.draw.line(screen, black, (x, y), (x+100, y+100), 6)
        pygame.draw.line(screen, black, (x+100, y), (x, y + 100), 6)
        turn += 1

    # DRAW 'O' IN CURRENT POSITION
    else:
        pygame.draw.circle(screen, black, (x+50, y+50), 50, 6)
        turn += 1


def turn_():
    # WHO PLAY NOW?
    if turn % 2 == 1:
        return 'x'
    return 'o'


def get_pos(y, x):
    # WHERE DRAW
    if y == 2:
        y = 350
        if x == 2:
            draw(y, 350)
        elif x == 1:
            draw(y, 250)
        elif x == 0:
            draw(y, 150)

    if y == 1:
        y = 250
        if x == 2:
            draw(y, 350)
        elif x == 1:
            draw(y, 250)
        elif x == 0:
            draw(y, 150)

    if y == 0:
        y = 150
        if x == 2:
            draw(y, 350)
        elif x == 1:
            draw(y, 250)
        elif x == 0:
            draw(y, 150)


def display_score():
    score_text = menu.text_format('score:', menu.font_alternative, 25, white)

    score_x = 'X: ' + str(score[0])
    score_x_display = menu.text_format(score_x, menu.font_alternative, 25, white)

    score_o = 'O: ' + str(score[1])
    score_o_display = menu.text_format(score_o, menu.font_alternative, 25, white)

    screen.blit(score_text, (0, 510))
    screen.blit(score_x_display, (0, 540))
    screen.blit(score_o_display, (0, 570))


def display_turn():
    global score

    now_turn = turn_()
    if now_turn == 'x':
        color_o = transparent
        color_x = white
    else:
        color_o = white
        color_x = transparent

    player = menu.text_format('Turn:', menu.font_alternative, 25, white)
    player_rect = player.get_rect()

    player_o = menu.text_format('o', menu.font_alternative, 25, color_o)
    player_x = menu.text_format('x', menu.font_alternative, 25, color_x)

    screen.blit(player, ((600-(player_rect[2]+15)), 570))
    screen.blit(player_o, ((600 - 12), 570))
    screen.blit(player_x, ((600 - 12), 570))


class pxp:
    def __init__(self):
        screen.fill(black)
        self.main()

    def main(self):
        global arrow_return, matriz_table, turn, score

        table()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    # WHERE YOU CLICK
                    # FROM BOTTOM TO UP
                    # ROW 1
                    if 350 <= y <= 450:
                        if 150 <= x < 250:
                            marked = check(2, 0)
                            if marked:
                                continue
                            matriz_table[2][0] = turn_()
                            get_pos(2, 0)
                        elif 250 <= x < 350:
                            marked = check(2, 1)
                            if marked:
                                continue
                            matriz_table[2][1] = turn_()
                            get_pos(2, 1)
                        elif 350 <= x <= 450:
                            marked = check(2, 2)
                            if marked:
                                continue
                            matriz_table[2][2] = turn_()
                            get_pos(2, 2)

                    # ROW 2
                    elif 250 <= y < 350:
                        if 150 <= x < 250:
                            marked = check(1, 0)
                            if marked:
                                continue
                            matriz_table[1][0] = turn_()
                            get_pos(1, 0)
                        elif 250 <= x < 350:
                            marked = check(1, 1)
                            if marked:
                                continue
                            matriz_table[1][1] = turn_()
                            get_pos(1, 1)
                        elif 350 <= x <= 450:
                            marked = check(1, 2)
                            if marked:
                                continue
                            matriz_table[1][2] = turn_()
                            get_pos(1, 2)

                    # ROW 3
                    elif 150 <= y < 250:
                        if 150 <= x < 250:
                            marked = check(0, 0)
                            if marked:
                                continue
                            matriz_table[0][0] = turn_()
                            get_pos(0, 0)
                        elif 250 <= x < 350:
                            marked = check(0, 1)
                            if marked:
                                continue
                            matriz_table[0][1] = turn_()
                            get_pos(0, 1)
                        elif 350 <= x <= 450:
                            marked = check(0, 2)
                            if marked:
                                continue
                            matriz_table[0][2] = turn_()
                            get_pos(0, 2)

                    # RETURN BUTTON ACTION
                    elif 0 <= x <= 50 and 0 <= y <= 40:
                        screen.fill(black)
                        matriz_table = [['-', '-', '-'],
                                        ['-', '-', '-'],
                                        ['-', '-', '-']]
                        turn = 1
                        score[0] = 0
                        score[1] = 0
                        menu.secondary_menu()

                    # HOME BUTTON ACTION
                    elif 560 <= x <= 600 and 0 <= y <= 40:
                        screen.fill(black)
                        matriz_table = [['-', '-', '-'],
                                        ['-', '-', '-'],
                                        ['-', '-', '-']]
                        turn = 1
                        score[0] = 0
                        score[1] = 0
                        menu.main_menu()

            home_button()
            arrow_button()
            display_score()
            display_turn()

            pygame.display.flip()
            clock.tick(tick)


class pxc:
    def __init__(self):
        screen.fill(black)
        self.main()

    def main(self):
        global arrow_return, matriz_table, turn, score, game

        table()
        game = 'pxc'

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # COM:
                if turn % 2 == 0:
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
                    marked = check(y, x)
                    if marked:
                        continue
                    matriz_table[y][x] = turn_()
                    get_pos(y, x)

                # PLAYER:
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos

                        # WHERE YOU CLICK
                        # FROM BOTTOM TO UP
                        # ROW 1
                        if 350 <= y <= 450:
                            if 150 <= x < 250:
                                marked = check(2, 0)
                                if marked:
                                    continue
                                matriz_table[2][0] = turn_()
                                get_pos(2, 0)
                            elif 250 <= x < 350:
                                marked = check(2, 1)
                                if marked:
                                    continue
                                matriz_table[2][1] = turn_()
                                get_pos(2, 1)
                            elif 350 <= x <= 450:
                                marked = check(2, 2)
                                if marked:
                                    continue
                                matriz_table[2][2] = turn_()
                                get_pos(2, 2)

                        # ROW 2
                        elif 250 <= y < 350:
                            if 150 <= x < 250:
                                marked = check(1, 0)
                                if marked:
                                    continue
                                matriz_table[1][0] = turn_()
                                get_pos(1, 0)
                            elif 250 <= x < 350:
                                marked = check(1, 1)
                                if marked:
                                    continue
                                matriz_table[1][1] = turn_()
                                get_pos(1, 1)
                            elif 350 <= x <= 450:
                                marked = check(1, 2)
                                if marked:
                                    continue
                                matriz_table[1][2] = turn_()
                                get_pos(1, 2)

                        # ROW 3
                        elif 150 <= y < 250:
                            if 150 <= x < 250:
                                marked = check(0, 0)
                                if marked:
                                    continue
                                matriz_table[0][0] = turn_()
                                get_pos(0, 0)
                            elif 250 <= x < 350:
                                marked = check(0, 1)
                                if marked:
                                    continue
                                matriz_table[0][1] = turn_()
                                get_pos(0, 1)
                            elif 350 <= x <= 450:
                                marked = check(0, 2)
                                if marked:
                                    continue
                                matriz_table[0][2] = turn_()
                                get_pos(0, 2)

                        # RETURN BUTTON ACTION
                        elif 0 <= x <= 50 and 0 <= y <= 40:
                            screen.fill(black)
                            matriz_table = [['-', '-', '-'],
                                            ['-', '-', '-'],
                                            ['-', '-', '-']]
                            # RESET
                            turn = 1
                            score[0] = 0
                            score[1] = 0
                            game = 'pxp'
                            menu.secondary_menu()

            arrow_button()
            display_score()

            pygame.display.flip()
            clock.tick(tick)

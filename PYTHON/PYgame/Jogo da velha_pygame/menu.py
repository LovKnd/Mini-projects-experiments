import random
import pygame
import main as m
import Game

pygame.init()
pygame.font.init()

# DISPLAY
global screen, clock, tick
screen = m.screen
clock = m.clock
tick = m.tick
selected = 'start'
selected_2 = 'player VS player'

# COLORS
global black, white, yellow
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 215, 0)

# FONTS
global font, font_title, font_alternative
font: str = "Font/Retro.ttf"
font_title = "Font/Retro.ttf"
font_alternative = "Font/Questrial-Regular.ttf"


# PLAYER VS PLAYER CALL
def pxp():
    Game.pxp()


# PLAYER VS COM CALL
def pxc():
    Game.pxc()


def text_format(message, textFont, textSize, textColor):  # Text Renderer
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


class secondary_menu:
    def __init__(self):
        self.main()

    def main(self):
        global selected_2

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # MENU SELECT
                if event.type == pygame.KEYDOWN:
                    if selected_2 == 'player VS player' and event.key == pygame.K_DOWN:
                        selected_2 = 'player VS COM'

                    elif selected_2 == 'player VS COM':
                        if event.key == pygame.K_DOWN:
                            selected_2 = 'return'
                        elif event.key == pygame.K_UP:
                            selected_2 = 'player VS player'

                    elif selected_2 == 'return' and event.key == pygame.K_UP:
                        selected_2 = 'player VS COM'

                    # TRIGGERED EVENT_BUTTON
                    if event.key == pygame.K_RETURN:
                        if selected_2 == "player VS player":
                            pxp()
                        if selected_2 == "player VS COM":
                            pxc()
                        if selected_2 == 'return':
                            m.main_menu()

            # BUTTON DISPLAY CONDITION
            if selected_2 == 'player VS player':
                text_pxp = text_format('Player VS Player', font, 75, yellow)
            else:
                text_pxp = text_format('Player VS Player', font, 75, white)

            if selected_2 == 'player VS COM':
                text_pxc = text_format('Player VS COM', font, 75, yellow)
            else:
                text_pxc = text_format('Player VS COM', font, 75, white)

            if selected_2 == 'return':
                text_return = text_format('Return', font, 75, yellow)
            else:
                text_return = text_format('Return', font, 75, white)

            pxp_rect = text_pxp.get_rect()
            pxc_rect = text_pxc.get_rect()
            return_rect = text_return.get_rect()

            screen.blit(text_pxp, (300 - (pxp_rect[2] / 2), 150))
            screen.blit(text_pxc, (300 - (pxc_rect[2] / 2), 250))
            screen.blit(text_return, (300 - (return_rect[2] / 2), 350))

            pygame.display.update()
            clock.tick(tick)


class main_menu:
    def __init__(self):

        # BACKGROUND
        self.stars_list = []
        self.star_generation()
        self.main()

    def star_generation(self):  # BACKGROUND
        # GENERATE THE STARS POSITION
        for i in range(50):
            x = random.randrange(0, 595)
            y = random.randrange(0, 595)
            self.stars_list.append([x, y])

    def create_stars(self):  # BACKGROUND
        # DISPLAY THE STARS
        for i in range(len(self.stars_list)):
            d = random.randint(1, 2)
            pygame.draw.circle(screen, white, self.stars_list[i], d)

    def background(self):
        # MY SIGNATURE
        signature = text_format('BY Pedro', font_alternative, 12, white)
        screen.blit(signature, (2, 585))

        # THE STARS IN MAIN MENU
        self.create_stars()

    def main(self):
        global selected

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # MENU SELECT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_DOWN:
                        selected = "quit"

                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            screen.fill(black)
                            secondary_menu.main(self)
                        if selected == "quit":
                            pygame.quit()
                            quit()

            screen.fill(black)
            self.background()

            title = text_format('Jogo Da Velha', font_title, 90, yellow)

            # BUTTON DISPLAY CONDITION
            if selected == "start":
                text_start = text_format('START', font, 75, yellow)
            else:
                text_start = text_format('START', font, 75, white)
            if selected == "quit":
                text_quit = text_format('QUIT', font, 75, yellow)
            else:
                text_quit = text_format('QUIT', font, 75, white)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            screen.blit(title, (300 - (title_rect[2] / 2), 80))
            screen.blit(text_start, (300 - (start_rect[2] / 2), 300))
            screen.blit(text_quit, (300 - (quit_rect[2] / 2), 360))

            pygame.display.flip()
            clock.tick(tick)

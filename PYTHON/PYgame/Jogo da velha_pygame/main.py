import pygame
import os
import menu

# DISPLAY
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da velha')
clock = pygame.time.Clock()
tick = 5


# Initialize the Game{
def main_menu():
    menu.main_menu()


if __name__ == '__main__':
    # CENTER THE WINDOW
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    main_menu()

    pygame.quit()
    quit()
# }

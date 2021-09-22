import pygame
import sys

pygame.init()

s = (300, 300)
screen = pygame.display.set_mode(s, pygame.RESIZABLE)
screen_x = s[0]
screen_y = s[1]

color_white = (255, 255, 255)
color_light = (180, 180, 180)
color_dark = (110, 110, 110)
black = (0, 0, 0)

smallfont = pygame.font.SysFont('Arial', 30)
text = smallfont.render('Quit', True, color_white)

while True:
    width = screen.get_width()
    height = screen.get_height()
    screen_x = width
    screen_y = height

    for e in pygame.event.get():
        if e.type == pygame.QUIT: 
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if width/2 - 70 <= mouse[0] <= width/2 + 70 and height/2 - 20 <= mouse[1] <= height/2 + 20:
                pygame.quit()

    screen.fill(black)
    mouse = pygame.mouse.get_pos() 

    if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20:
        pygame.draw.rect(screen, color_light, [width/2 - 70, height/2 - 20, 140, 40])
    else: 
        pygame.draw.rect(screen, color_dark, [width/2 - 70, height/2 - 20, 140, 40])

    screen.blit(text, (width/2-70+40, height/2-20))
    pygame.display.flip()
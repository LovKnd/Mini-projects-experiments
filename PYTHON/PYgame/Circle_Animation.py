import pygame
import sys
from pygame.locals import *
Green = (0, 255, 0)
Black = (0, 0, 0)
FPS = 50
fpsClock = pygame.time.Clock()
x_Pos = 300
y_Pos = 250
x_Vel = -5
y_Vel = 5
pygame.init()
Display= pygame.display.set_mode((500, 400))
pygame.display.set_caption('Animation')
while True:
    Display.fill(Black)
    pygame.draw.circle(Display,Green, (x_Pos, y_Pos), 10, 0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    x_Pos += x_Vel
    y_Pos += y_Vel
    if x_Pos > 490 or x_Pos <10:
        x_Vel *= -1
    if y_Pos >390 or y_Pos <10:
        y_Vel *= -1
    pygame.display.update()
    fpsClock.tick(FPS)
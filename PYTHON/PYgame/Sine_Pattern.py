import math
import pygame
pygame.init()
scr = pygame.display.set_mode((380,400))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    t = pygame.time.get_ticks() / 2 % 400
    x = t
    y = math.sin(t/50.0) * 100 + 200
    y = int(y)
    scr.fill((0,0,0))
    pygame.draw.circle(scr, (255,255,255), (x, y), 30)
    pygame.display.flip()
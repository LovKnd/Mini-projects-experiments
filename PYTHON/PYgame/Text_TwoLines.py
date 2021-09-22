import pygame
pygame.init()
Size = WIDTH, HEIGHT = (900, 700)
FPS = 30
scr = pygame.display.set_mode(Size, pygame.RESIZABLE)
clock = pygame.time.Clock()
def blit_text(surface, text, pos, font, color=pygame.Color('blue')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height
text ="Welcome to python tutorial.\nHere you will learn about pygame"
font = pygame.font.SysFont('Arial', 70)
while True:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    scr.fill(pygame.Color('black'))
    blit_text(scr, text, (20, 20), font)
    pygame.display.update()
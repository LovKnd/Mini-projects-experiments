import pygame,sys
pygame.init()
clock = pygame.time.Clock()
scr = pygame.display.set_mode([500,500])
base_font = pygame.font.Font(None,32)
user_text = ""
input_rect = pygame.Rect(200,200,140,32)
color_active = pygame.Color("Green")
color_passive = pygame.Color("yellow")
color = color_passive
active = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
    scr.fill((0,0,0))
    if active:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(scr,color,input_rect,2)
    text_surface = base_font.render(user_text,True,(255,255,255))
    scr.blit(text_surface,(input_rect.x + 5,input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)
    pygame.display.flip()
    clock.tick(50)
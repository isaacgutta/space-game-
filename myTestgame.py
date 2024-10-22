import pygame

# setup
pygame.init()
WINDOW_WIDTH, WINDOW_HIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pygame.display.set_caption('space shooter')
running = True

surf = pygame.surface((100,200))

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
     #draw the game 
    display_surface.fill('dark gray')
    display_surface.blit(surf, (100,150))
    pygame.display.update()
    
pygame.quit()


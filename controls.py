import pygame, sys
from shot import Shot

def events(screen, ship, shots):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #right
            if event.key == pygame.K_d:
                ship.mright = True
            #left
            elif event.key == pygame.K_a:
                ship.mleft = True
            #shot
            elif event.key == pygame.K_SPACE:
                new_bullet = Shot(screen, ship)
                shots.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #right
            if event.key == pygame.K_d:
                ship.mright = False
            #left
            elif event.key == pygame.K_a:
                ship.mleft = False

def update(bg_color, screen, ship, shots):
    """обновления экрана"""
    screen.fill(bg_color)
    for shot in shots.sprites():
        shot.draw_shot()
    ship.output()
    pygame.display.flip()
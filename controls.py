import pygame, sys

def events(ship):
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
        elif event.type == pygame.KEYUP:
            #right
            if event.key == pygame.K_d:
                ship.mright = False
            #left
            elif event.key == pygame.K_a:
                ship.mleft = False
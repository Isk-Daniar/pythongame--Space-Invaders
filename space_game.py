import pygame, controls
from ship import Ship

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    ship = Ship(screen)

    while True:
        controls.events(ship)
        ship.update_ship()
        screen.fill(bg_color)
        ship.output()
        pygame.display.flip()

run()
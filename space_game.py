import pygame, controls
from ship import Ship
from pygame.sprite import Group
from stats import Stats

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    ship = Ship(screen)
    shots = Group()
    enemies = Group()
    controls.create_army(screen, enemies)
    stats = Stats()

    while True:
        controls.events(screen, ship, shots)
        ship.update_ship()
        controls.update(bg_color, screen, ship, enemies, shots)
        controls.update_shots(screen, enemies, shots)
        controls.update_enemies(stats, screen, ship, enemies, shots)

run()
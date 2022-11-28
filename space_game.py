import pygame, controls
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from score import Scores

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
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, ship, shots)
        if stats.run_game:
            ship.update_ship()
            controls.update(bg_color, screen, stats, sc, ship, enemies, shots)
            controls.update_shots(screen, stats, sc, enemies, shots)
            controls.update_enemies(stats, screen, sc, ship, enemies, shots)

run()
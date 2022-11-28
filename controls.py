import pygame, sys
from shot import Shot
from enemy import Enemy
import time

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

def update(bg_color, screen, stats, sc, ship, enemies, shots):
    """обновления экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for shot in shots.sprites():
        shot.draw_shot()
    ship.output()
    enemies.draw(screen)
    pygame.display.flip()

def update_shots(screen, stats, sc, enemies, shots):
    """обновления позиции пуль"""
    shots.update()
    for shot in shots.copy():
        if shot.rect.bottom <= 0:
            shots.remove(shot)
    collisions = pygame.sprite.groupcollide(shots,enemies, True, True)
    if collisions:
        for enemies in collisions.values():
            stats.score += 5 * len(enemies)
        stats.score += 10
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_ships()
    if len(enemies) == 0:
        shots.empty()
        create_army(screen, enemies)

def ship_kill (stats, screen, sc, ship, enemies, shots):
    """столкновения корабля и армии"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sc.image_ships()
        enemies.empty()
        shots.empty()
        create_army(screen, enemies)
        ship.create_ship()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_enemies(stats, screen, sc, ship, enemies, shots):
    """обновления позиции врагов"""
    enemies.update()
    if pygame.sprite.spritecollideany(ship, enemies):
        ship_kill(stats, screen, sc, ship, enemies, shots)
    enemies_check(stats, screen, sc, ship, enemies, shots)

def enemies_check(stats, screen, sc, ship, enemies, shots):
    """проверка, добралась ли армия до края экрна"""
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            ship_kill(stats, screen, sc, ship, enemies, shots)
            break

def create_army(screen, enemies):
    """создания армию"""
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((700 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 500 - 2) / enemy_height)

    for row_number in range(number_enemy_y - 5):

        for enemy_number in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + enemy_width * enemy_number
            enemy.y = enemy_height + enemy_height * row_number
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + enemy.rect.height * row_number
            enemies.add(enemy)

def check_high_score(stats, sc):
    """проверка рекорда"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score ))
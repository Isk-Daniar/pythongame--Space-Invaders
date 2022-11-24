import pygame, sys
from shot import Shot
from enemy import Enemy

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

def update(bg_color, screen, ship, enemies, shots):
    """обновления экрана"""
    screen.fill(bg_color)
    for shot in shots.sprites():
        shot.draw_shot()
    ship.output()
    enemies.draw(screen)
    pygame.display.flip()

def update_shots(enemies, shots):
    """обновления позиции пуль"""
    shots.update()
    for shot in shots.copy():
        if shot.rect.bottom <= 0:
            shots.remove(shot)
    collisions = pygame.sprite.groupcollide(shots,enemies, True, True)

def update_enemies(ship, enemies):
    """обновления позиции врагов"""
    enemies.update()
    if pygame.sprite.spritecollideany(ship, enemies):
        print('!!!!!!!!!!!')

def create_army(screen, enemies):
    """создания армию"""
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((700 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 100 - 2) / enemy_height)

    for row_number in range(number_enemy_y - 5):

        for enemy_number in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + enemy_width * enemy_number
            enemy.y = enemy_height + enemy_height * row_number
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + enemy.rect.height * row_number
            enemies.add(enemy)
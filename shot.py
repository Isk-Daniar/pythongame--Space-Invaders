import pygame

class Shot(pygame.sprite.Sprite):

    def __init__(self, screen, ship):
        """"создания пулю в позиции пушки"""
        super(Shot, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 400, 12)
        self.color = (0, 187, 212)
        self.speed = 4.5
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_shot(self):
        """рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
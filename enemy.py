import pygame

class Enemy(pygame.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self, screen):
        """инициализируем и задаем начальную позицию"""
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("img/enemy-1.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод врага на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещени врагов"""
        self.y += 0.1
        self.rect.y = self.y
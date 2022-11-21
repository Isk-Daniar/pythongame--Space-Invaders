import pygame

class Ship():
    def __init__(self, screen):
        """инициалищация корабля"""

        self.screen = screen
        self.img = pygame.image.load("img/pixil-frame-1.png")
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """отображение корабля"""
        self.screen.blit(self.img, self.rect)

    def update_ship(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.mleft and self.rect.left >0:
            self.rect.centerx -= 1
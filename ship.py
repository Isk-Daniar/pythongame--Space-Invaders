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

    def output(self):
        """отображение корабля"""
        self.screen.blit(self.img, self.rect)
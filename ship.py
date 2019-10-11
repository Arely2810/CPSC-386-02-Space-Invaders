import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, settings, screen):
        super(Ship, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        r, sr = self.rect, self.screen_rect
        r.centerx = sr.centerx
        r.bottom = sr.bottom
        self.settings = settings
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed
        self.rect.centerx and self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

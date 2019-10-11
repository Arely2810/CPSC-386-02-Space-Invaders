import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.ship_rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.ship_rect.centerx = ship.rect.centerx
        self.ship_rect.top = ship.rect.top

        self.y = float(self.ship_rect.y)

        self.color = settings.bullet_color
        self.speed_ = settings.bullet_speed

    def update(self):
        self.y -= self.speed_
        self.ship_rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.ship_rect)

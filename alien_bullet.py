import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    def __init__(self, settings, screen, alien):
        super(AlienBullet, self).__init__()
        self.screen = screen
        self.alien_x = alien.rect.x
        self.alien_y = alien.rect.y

        self.alien_rect = pygame.Rect(self.alien_x, self.alien_y, settings.bullet_width, settings.bullet_height)
        self.alien_rect.centerx = alien.rect.centerx
        self.alien_rect.top = alien.rect.top

        self.y = float(self.alien_rect.y)

        self.color = settings.bullet_color
        self.speed_ = settings.bullet_speed

    def update(self):
        self.y += self.speed_
        self.alien_rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.alien_rect)

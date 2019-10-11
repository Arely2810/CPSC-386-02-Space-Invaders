import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = pygame.Color('#000000')
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 207, 241
        self.bullets_allowed = 4
        self.fleet_drop = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        self.fleet_direction = 1
        self.alien1_points = 50
        self.alien2_points = 60
        self.alien3_points = 70
        self.ufo_points = 100

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien1_points = int(self.alien1_points * self.score_scale)
        self.alien2_points = int(self.alien2_points * self.score_scale)
        self.alien3_points = int(self.alien3_points * self.score_scale)
        self.ufo_points = int(self.ufo_points * self.score_scale)
        print(self.alien1_points + self.alien2_points + self.alien3_points + self.ufo_points)

    def dims(self):
        return self.screen_width, self.screen_height


import pygame.font


class StartScreen:
    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.black = (0, 0, 0)
        # self.end_it = False
        self.my_rect = pygame.Rect(400, 20, 400, 80)
        self.screen_font = pygame.font.SysFont(None, 70)
        self.text_color = (255, 255, 255)

    def start_screen(self):
        self.screen.fill(self.black)
        self.start_ = self.screen_font.render('Space Invaders', True, self.text_color, self.black)
        self.start_image = self.my_rect.get_rect()
        self.start_image.center = self.my_rect.center
        self.screen.blit(self.start_, self.start_image)

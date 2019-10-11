import pygame.font


class Button:
    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.black = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont(None, 45)
        self.button_rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_rect.center = self.screen_rect.center
        self.prep_msg(msg)
        # black = (0, 0, 0)
        # end_it = False
        # while (end_it == False):
        #     window.fill(black)
        #     myfont = pygame.font.SysFont("Space Invaders", 70)
        #     for event in pygame.event.get():
        #         if event.type == MOUSEBUTTONDOWN:
        #             end_it = True
        #     window.blit(nlabel, (200, 200))
        #     pygame.display.flip()

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)









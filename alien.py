import pygame
from timer import Timer
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings, screen, images):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        self.image = []
        for pic in images:
            self.image.append(pygame.image.load(pic))
        # self.alien1_images = ['images/begin_alien.png', 'images/begin_alien2.png']
        # self.alien2_images = ['images/second_alien.png', 'images/second_alien2.png']
        # self.alien3_images = ['images/third_alien.png', 'images/third_alien2.png']
        # self.ufo_images = ['images/ufo.png', 'images/ufo2.png']
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


        # for pic in self.image:
        #     self.rect.append(pic.get_rect())
        # for re in self.rect:
        #     re.x = self.rect.width
        #     re.y = self.rect.height
        #     self.x = float(re.x)

        # self.animate_alien1 = Timer(frames=self.alien1_images, wait=100, frameindex=0, step=1, looponce=False)
        # self.animate_alien2 = Timer(frames=self.alien2_images, wait=100, frameindex=0, step=1, looponce=False)
        # self.animate_alien3 = Timer(frames=self.alien3_images, wait=100, frameindex=0, step=1, looponce=False)
        # self.animate_ufo = Timer(frames=self.ufo_images, wait=100, frameindex=0, step=1, looponce=False)
        #
        # self.alien1_rect = self.animate_alien1.imagerect().get_rect()
        # self.alien1_rect.x = self.alien1_rect.width
        # self.alien1_rect.y = self.alien1_rect.height
        #
        # self.alien2_rect = self.animate_alien2.imagerect().get_rect()
        # self.alien2_rect.x = self.alien2_rect.width
        # self.alien2_rect.y = self.alien2_rect.height
        #
        # self.alien3_rect = self.animate_alien3.imagerect().get_rect()
        # self.alien3_rect.x = self.alien3_rect.width
        # self.alien3_rect.y = self.alien3_rect.height
        #
        # self.ufo_rect = self.animate_ufo.imagerect().get_rect()
        # self.ufo_rect.x = self.ufo_rect.width
        # self.ufo_rect.y = self.ufo_rect.height
        #
        # self.alien1_x = float(self.alien1_rect.x)
        # self.alien2_x = float(self.alien2_rect.x)
        # self.alien3_x = float(self.alien3_rect.x)
        # self.ufo_x = float(self.ufo_rect.x)

        self.explode_images = ['images/explosion1.png', 'images/explosion2.png', 'images/explosion3.png',
                               'images/explosion4.png', 'images/explosion5.png', 'images/explosion6.png']
        self.ex = Timer(frames=self.explode_images, wait=100, frameindex=0, step=1, looponce=True)
        self.ex_rect = self.rect


    def blitme(self):
        # self.screen.blit(self.alien1_images, self.alien1_rect)
        # self.screen.blit(self.alien2_images, self.alien2_rect)
        # self.screen.blit(self.alien3_images, self.alien3_rect)
        # self.screen.blit(self.ufo_images, self.ufo_rect)
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def explosion(self):
        self.screen.blit(self.explode_images, self.ex_rect)

    def points(self):
        raise NotImplementedError

import pygame
import sys
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from gamestats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.dims())
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    # alien = Alien(settings, screen)
    play_button = Button(settings, screen, "Play")
    high_scores = Button(settings, screen, "High Scores")

    gf.create_fleet(settings, screen, ship, aliens)

    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    game_over = False
    while not game_over:
        gf.check_events(settings, screen, stats, sb, play_button, high_scores, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button, high_scores)


run_game()

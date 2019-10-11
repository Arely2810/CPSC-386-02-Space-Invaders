import sys
import pygame
from bullet import Bullet
from alien_bullet import AlienBullet
from alien import Alien
from time import sleep
from pygame.sprite import Sprite

def check_events(settings, screen, stats, sb, play_button, high_scores, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
            check_high_button(settings, screen,stats, high_scores, mouse_x, mouse_y)


def check_high_button(settings, screen, stats, high_scores, mouse_x, mouse_y):
    button_clicked = high_scores.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        grey = (51, 54, 52)
        text_color = (255, 255, 255)

        best_rect = pygame.Rect(400, 50, 400, 50)
        screen_font = pygame.font.SysFont(None, 50)
        screen.fill(grey)
        high = screen_font.render('The Best 10', True, text_color, grey)
        high_image = best_rect.get_rect()
        high_image.center = best_rect.center
        screen.blit(high, high_image)

        input_file = open('best.txt', 'r')
        text = []
        for line in input_file:
            text.append(line)
        text = '\n'.join(text)
        scores_rect = pygame.Rect(350, 100, 500, 550)
        screen.fill(grey)
        score = screen_font.render(text, True, text_color, grey)
        score_image = scores_rect.get_rect()
        score_image.center = scores_rect.center
        screen.blit(score, score_image)


def check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets,mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, bullets)
        ship.center_ship()

def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < settings.bullets_allowed:
            new_bullet = Bullet(settings, screen, ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    alien1_images = ['images/begin_alien.png', 'images/begin_alien2.png']

    temp = Alien(settings, screen, alien1_images)
    temp.explosion()
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien1_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(settings, screen, ship, aliens)

def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(settings, screen, ship, aliens):
    alien1_images = ['images/begin_alien.png', 'images/begin_alien2.png']
    alien2_images = ['images/second_alien.png', 'images/second_alien2.png']
    alien3_images = ['images/third_alien.png', 'images/third_alien2.png']
    alien1 = Alien(settings, screen, alien1_images)
    alien2 = Alien(settings, screen, alien2_images)
    alien3 = Alien(settings, screen, alien3_images)
    aliens_ = [alien1, alien2, alien3]
    for alien in aliens_:
        number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
        number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                create_alien(settings, screen, aliens, alien_number, row_number, aliens_)

def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number, aliens_):
    # alien = Alien(settings, screen, images)
    for alien in aliens_:
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)


def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop
    settings.fleet_direction *= -1


def update_aliens(settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(settings, screen, stats, sb, ship, aliens, bullets)


def ship_hit(settings, screen, stats, sb, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(settings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, screen, stats, sb, ship, aliens, bullets)
            break




import sys
import pygame
from bullet import Bullet
from ufo import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets,stats,aliens):
    if event.key==pygame.K_RIGHT: #Right side
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_p and not stats.game_active:
        start_game(stats,aliens,bullets,ai_settings,screen,ship)
def check_keyup_event(event,ship):
    if event.key==pygame.K_RIGHT: #Right side
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

def check_events(ai_settings,screen,ship,bullets,play_button,stats,aliens):
    #Getting the actions from keyboard and mouse
    for event in pygame.event.get(): #Check for a present action
            if event.type==pygame.QUIT: #Exit
                sys.exit()
            elif event.type==pygame.KEYDOWN: #If pressed
                check_keydown_events(event,ai_settings,screen,ship,bullets,stats,aliens)
            elif event.type==pygame.KEYUP: #If unpressed
                check_keyup_event(event,ship)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(play_button,stats,mouse_x,mouse_y,aliens,bullets,ship,ai_settings,screen)

def update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats):
    screen.fill(ai_settings.bg_color) #Fill with the colour
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip() #Show the window

def check_play_button(play_button,stats,mouse_x,mouse_y,aliens,bullets,ship,ai_settings,screen):
    play_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if play_clicked and not stats.game_active:
        start_game(stats,aliens,bullets,ai_settings,screen,ship)

def start_game(stats,aliens,bullets,ai_settings,screen,ship):
    pygame.mouse.set_visible(False)
    stats.reset_stat()
    stats.game_active = True

    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings,screen,aliens,ship)
    ship.center_ship()

def update_bullets(bullets, aliens, ai_settings, screen, ship):
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    check_bullets_collision(bullets, aliens, ai_settings, screen, ship)

def check_bullets_collision(bullets, aliens, ai_settings, screen, ship,):
    collisions = pygame.sprite.groupcollide(bullets,aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
    available_space = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space/(2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(screen,ai_settings,aliens,alien_number, row_number):
    alien = Alien(screen,ai_settings)
    alien_width = alien.rect.width  
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens,ship):
    alien = Alien(screen,ai_settings)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,alien.rect.height,ship.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(screen,ai_settings,aliens,alien_number, row_number)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_rate
    ai_settings.fleet_direction *= -1

def ship_hit(aliens,stats,ai_settings,ship,screen,bullets):
    if stats.ship_left > 0:
        stats.ship_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()

        sleep(0.5)
    else:
        pygame.mouse.set_visible(True)
        stats.game_active = False

def update_aliens(aliens,stats,ai_settings,ship,screen,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(aliens,stats,ai_settings,ship,screen,bullets)
    check_aliends_bottom(aliens,stats,ai_settings,ship,screen,bullets)

def check_aliends_bottom(aliens,stats,ai_settings,ship,screen,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(aliens,stats,ai_settings,ship,screen,bullets)
            break
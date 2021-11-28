import sys
import pygame
from bullet import Bullet
from star import Star
from random import randint

def change_flag_keydown(event,hero,screen,g_settings,bullets):
    '''
    if event.key==pygame.K_RIGHT:
        hero.move_right=True
    elif event.key==pygame.K_LEFT:
        hero.move_left=True
    '''
    if event.key==pygame.K_UP:
        hero.move_up=True
    elif event.key==pygame.K_DOWN:
        hero.move_down=True
    elif event.key == pygame.K_SPACE:
        fire_bullet(g_settings,bullets,screen,hero)

def change_flag_keyup(event,hero):
    '''
    if event.key==pygame.K_RIGHT:
        hero.move_right=False
    elif event.key==pygame.K_LEFT:
        hero.move_left=False
    '''
    if event.key==pygame.K_UP:
        hero.move_up=False
    elif event.key==pygame.K_DOWN:
        hero.move_down=False

def check_events(hero,screen,g_settings,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            change_flag_keydown(event,hero,screen,g_settings,bullets)
        elif event.type==pygame.KEYUP:
            change_flag_keyup(event,hero)

def update_screen(g_settings,hero,screen,bullets,stars):
    screen.blit(g_settings.image,hero.screen_rect)
    for bullet in bullets.sprites():
        bullet.draw_bullet(g_settings)
    stars.draw(screen)
    hero.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    for bullet in bullets.sprites():
        if bullet.rect.left >=1200:
            bullets.remove(bullet)

def fire_bullet(g_settings,bullets,screen,hero):
    if len(bullets) < g_settings.bullet_allowed:
            new_bullet = Bullet(screen,g_settings,hero)
            bullets.add(new_bullet)

def get_number_stars_x(g_settings,hero_width,star_width):
    available_space_x = g_settings.width - hero_width - (20 * star_width)
    number_stars = int(available_space_x / (2 * star_width) )
    return number_stars

def get_number_rows(g_settings,star_height):
    available_space_y = g_settings.height - 2 * star_height
    print(available_space_y)
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows
    

def create_star(screen, g_settings, stars, hero_width, star_number, row_number):
    star = Star(screen,g_settings)
    random_number = randint(-20,20)
    star_width = star.rect.width
    star.x = star_width * 13  + 3 * star_width * star_number + random_number
    star.rect.x = star.x
    star.rect.y = star.rect.height * row_number + random_number - 390
    stars.add(star)
    
def create_grid_star(screen,g_settings,hero,stars):
    star = Star(screen,g_settings)
    number_stars = get_number_stars_x(g_settings,hero.rect.width,star.rect.width)
    number_rows = get_number_rows(g_settings,star.rect.height)

    for row_number in range(number_rows):
        for star_number in range(number_stars):
            create_star(screen,g_settings,stars,hero.rect.width, star_number, row_number)

def check_stars_edges(screen,g_settings,hero,stars):
    for star in stars.sprites():
        if star.check_edges():
            g_settings.allowance_new_row = True
            break

def remove_stars(stars):
    for star in stars.sprites():
        if star.check_edges():
            stars.remove(star)

def update_stars(stars,g_settings,screen,hero):
    #if g_settings.allowance_new_row == False:
    #    check_stars_edges(screen,g_settings,hero,stars)
    remove_stars(stars)
    if len(stars) == 0:
        create_grid_star(screen,g_settings,hero,stars)
    stars.update()


        
    
        
        

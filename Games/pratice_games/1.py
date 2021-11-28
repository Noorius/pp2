import pygame
from settings import Settings
import functions as foo
from hero import Hero
from pygame.sprite import Group
from bullet import Bullet

def run_game():
    pygame.init()
    g_settings = Settings()
    screen = pygame.display.set_mode((g_settings.width,g_settings.height))
    pygame.display.set_caption('Practice window')
    hero = Hero(screen,g_settings)
    bullets = Group()
    stars = Group()

    foo.create_grid_star(screen,g_settings,hero,stars)

    while True:
        foo.check_events(hero,screen,g_settings,bullets)
        hero.update()
        bullets.update(g_settings)
        foo.update_bullets(bullets)
        foo.update_stars(stars,g_settings,screen,hero)
        foo.update_screen(g_settings,hero,screen,bullets,stars)
        
    
run_game()
import pygame
from setting import Setting
from cather import Cather
import functions as foo
from pygame.sprite import Group
from stats import GameStats

pygame.init()

g_setting = Setting()
screen = pygame.display.set_mode((g_setting.width,g_setting.height))
catcher = Cather(screen,g_setting)
objects = Group()
products = Group()
stats = GameStats(g_setting)

while True:
    foo.check_event(catcher,g_setting)
    if g_setting.game_active:
        catcher.update()

        objects.update()
        foo.update_objects(objects,screen,g_setting,catcher)

        products.update()
        foo.update_products(products,screen,g_setting,catcher)

        foo.check_collision(catcher,objects,products,stats,g_setting)

    foo.update_screen(screen,catcher,objects,products,g_setting,stats)
    pygame.display.flip()
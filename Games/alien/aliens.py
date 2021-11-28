import pygame
from Settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from ufo import Alien
from game_stat import GameStat
from button import Button

def run_game():
    #Creates screen object
    pygame.init() #Initial Settings
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #Object with screen and its size
    pygame.display.set_caption("Alien Invasion!") #Title on the Window

    play_button = Button(screen,ai_settings,"Play")
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    stats = GameStat(ai_settings)

    gf.create_fleet(ai_settings, screen,aliens,ship)

    while True: #The game cycle
        gf.check_events(ai_settings,screen,ship,bullets,play_button,stats,aliens)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_aliens(aliens,stats,ai_settings,ship,screen,bullets)
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
        
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats)
        

run_game()
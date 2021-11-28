import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen, g_settings,hero):
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0,0, g_settings.bullet_width, g_settings.bullet_height)
        self.screen_rect = screen.get_rect()
        self.rect.centery = hero.rect.centery

        
        self.x = float(self.rect.centerx)

    def update(self,g_settings):
        self.x += g_settings.bullet_speed_rate
        self.rect.centerx = self.x

    def draw_bullet(self,g_settings):
        pygame.draw.rect(self.screen,g_settings.bullet_color,self.rect)
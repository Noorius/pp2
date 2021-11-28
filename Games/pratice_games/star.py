import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self,screen,g_settings):
        super().__init__()
        self.screen = screen
        self.setting = g_settings

        self.image = pygame.image.load('pics/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.y = float(self.rect.y)
        self.y += self.setting.star_drop_rate
        self.rect.y = self.y
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True
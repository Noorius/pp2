from pygame.sprite import Sprite
import pygame
from random import randint

class Product(Sprite):
    def __init__(self,screen,g_setting):
        super().__init__()
        self.screen = screen
        self.g_setting = g_setting

        self.image = pygame.image.load('images/food/cherry.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        random_number = randint(0,self.g_setting.width - self.rect.width)
        self.rect.x = random_number
        self.rect.y = self.screen_rect.top - self.rect.height + randint(0,20)

        self.y = float(self.rect.y)

        self.drop_speed = randint(20,30) * 0.1
    
    def update(self):
        self.y += self.drop_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)
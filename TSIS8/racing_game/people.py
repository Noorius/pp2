from pygame.sprite import Sprite
import pygame
import os
from random import choice,randint,randrange

class Human(Sprite):
    def __init__(self,screen,g_settings):
        super().__init__()
        self.screen = screen 
        self.g_settings = g_settings
        self.speed = float(randint(10,20)/10)

        listi = os.listdir('images/people')
        self.image = pygame.image.load('images/people/'+choice(listi))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.bottom = self.screen_rect.top
        self.rect.x = randrange(0,self.g_settings.width,75)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)

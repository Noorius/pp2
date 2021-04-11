from pygame.sprite import Sprite
from random import randint,randrange
import pygame
from people import Human

class Coin(Human): #Ingeritates everything from Human because they a similar
    def __init__(self,screen,g_settings):
        super().__init__(screen,g_settings)
        self.sound = pygame.mixer.Sound('sounds/coin.wav') #New sound

        self.image = pygame.image.load('images/money.png') #New image
        self.rect = self.image.get_rect() #New rectangle
        
        self.rect.centerx = randrange(37,self.g_settings.width,75) #New x-coor

    #Functions for moving and blitting are the same
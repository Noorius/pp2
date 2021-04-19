import random
import pygame

class Food:

    def __init__(self,settings):
        self.sett = settings
        self.x = 0
        self.y = 0
        self.new_coor()

    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,0),(self.x,self.y,self.sett.block_size,self.sett.block_size))

    def new_coor(self):
        self.x = random.randrange(20, self.sett.width-20, self.sett.block_size)
        self.y = random.randrange(20, self.sett.height-20, self.sett.block_size)
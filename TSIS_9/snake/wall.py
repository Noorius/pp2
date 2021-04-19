import pygame

class Wall:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('wall.bmp')
        self.rect = self.image.get_rect()
    
    def blit(self,screen):
        screen.blit(self.image,self.rect)
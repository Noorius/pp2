import pygame

class Color:
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.fill = (0,255,0)
        self.rect = pygame.Rect(self.x,self.y,40,40)
        self.surface = pygame.Surface((40,40))

    def show_me(self):
        self.screen.blit(self.surface,self.rect)
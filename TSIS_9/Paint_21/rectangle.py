import pygame

class Rectangle:
    def __init__(self,screen,setting):
        self.setting = setting
        self.screen = screen
        self.x = self.setting.prev[0]
        self.y = self.setting.prev[1]
        self.width = self.setting.cur[0]-self.setting.prev[0]
        self. height = self.setting.cur[1]-setting.prev[1]

        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

        self.inner_rect = pygame.Rect(self.x+2, self.y+2,self.width-5,self.height-5)
        self.outer_rect = pygame.Rect(self.x-3, self.y-3,self.width+10,self.height+10)
        
    def blitme(self):
        pygame.draw.rect(self.screen,self.setting.drawing_color,self.rect,3)
        pygame.draw.rect(self.screen,self.setting.back_color,self.inner_rect)
        pygame.draw.rect(self.screen,self.setting.back_color,self.outer_rect,5)


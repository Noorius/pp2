import pygame

class Hero:
    def __init__(self,screen,g_settings):
        self.screen = screen
        self.setting = g_settings

        self.image = pygame.image.load('pics/hero.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        
        #self.xcoor = float(self.rect.centerx)
        self.ycoor = float(self.rect.centery)
        #self.move_right=False
        #self.move_left=False
        self.move_up=False
        self.move_down=False

    def update(self):
        '''
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.xcoor += self.setting.speed_rate
        if self.move_left and self.rect.left > 0:
            self.xcoor -= self.setting.speed_rate
        '''
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.ycoor -= self.setting.speed_rate
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.ycoor += self.setting.speed_rate
        #if not self.move_up and self.rect.bottom < self.screen_rect.bottom:
        #    self.ycoor +=0.5

        #self.rect.centerx = self.xcoor
        self.rect.centery = self.ycoor

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    
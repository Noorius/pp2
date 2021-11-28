import pygame

class Cather:
    def __init__(self, screen, g_setting):
        self.screen = screen
        self.g_setting = g_setting

        self.image = pygame.image.load('images/no.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.x = float(self.rect.centerx)

        self.open_mouth = False
        self.health = 100
    
    def update(self):
        self.health -= 0.01
        if self.g_setting.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.g_setting.cather_speed
        if self.g_setting.move_left and self.rect.left > 0:
            self.x -= self.g_setting.cather_speed
        self.rect.x = self.x

    def check_mouth(self):
        self.image = pygame.image.load('images/yes.bmp') if self.open_mouth else pygame.image.load('images/no.bmp')
    
    def blitme(self):
        self.check_mouth()
        self.screen.blit(self.image,self.rect)

    def center_catcher(self):
        self.x = self.screen_rect.centerx
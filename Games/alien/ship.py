import pygame

class Ship:
    def __init__(self,ai_settings,screen):
        self.screen = screen #Initial Position
        self.ai_settings = ai_settings
        #Image load and rect creating
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Appearance
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx) #Saving float number of a coordinate

        self.moving_right = False #Flag of movement to the right
        self.moving_left = False # to the left

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.center += self.ai_settings.ship_speed_factor # x-coor increases by speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor # x-coor deacreases by speed factor

        self.rect.centerx = self.center #Updating rect atribute based on self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx


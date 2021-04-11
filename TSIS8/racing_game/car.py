import pygame


class Car():
    def __init__(self,screen,g_settings):
        self.screen = screen
        self.g_settings = g_settings

        self.original_image = pygame.image.load('images/car.bmp')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.angle = 0

        self.rect.x = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        self.xcoor = float(self.rect.x)
        self.ycoor = float(self.rect.y)

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.sound_crash = pygame.mixer.Sound('sounds/crash.wav')
        self.sound_revive = pygame.mixer.Sound('sounds/engine.mp3')
        self.sound_beep = pygame.mixer.Sound('sounds/beep.wav')

    def update(self):
        if self.move_right and self.rect.right<self.g_settings.width: 
            if self.angle > -25 and self.rotate(-1):
                self.xcoor +=self.g_settings.speed_left_right
        if self.move_left and self.rect.x>0: 
            if self.angle < 25 and self.rotate(1):
                self.xcoor -=self.g_settings.speed_left_right
        if self.move_up:
            self.ycoor -= self.g_settings.speed_car
        if self.move_down:
            self.ycoor += self.g_settings.speed_car
        if not self.move_up:
            self.ycoor += 0.5

        self.rect.y = self.ycoor
        self.rect.x = self.xcoor
        self.return_0_angle()
        
    def return_0_angle(self):
        if self.angle>0:
            self.angle -= 0.5
        elif self.angle<0:
            self.angle += 0.5
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        
    def rotate(self,direction):
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.angle += 1 * direction
        if self.angle == 25 * direction:
            return True

    def center_car(self):
        self.xcoor = self.screen_rect.centerx
        self.ycoor = self.g_settings.height - self.rect.height - 30

    def blitme(self):
        self.screen.blit(self.image,self.rect)
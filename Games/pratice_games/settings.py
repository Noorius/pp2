import pygame

class Settings:
    def __init__(self):
        self.width=1200
        self.height=800
        self.bg_color=(0,0,230)
        self.image = pygame.image.load('pics/back.jpg')
        self.speed_rate = 2

        self.bullet_speed_rate = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        self.star_drop_rate = 1
        self.allowance_new_row = False
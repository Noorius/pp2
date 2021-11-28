import pygame

class Setting:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.background = pygame.image.load('images/background2.bmp')
        self.game_active = True
        self.lifes = 3

        self.cather_speed = 3
        self.move_left = False
        self.move_right = False

        #self.drop_speed = 1
        self.allowed_drops = 3

        self.font = pygame.font.SysFont('arial',30)
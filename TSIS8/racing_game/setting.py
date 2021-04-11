import pygame
from random import randint

class Settting:
    def __init__(self):
        self.game_active = True
        self.width = 1200
        self.height = 800
        self.back_colour = (159,159,159)
        self.font = pygame.font.SysFont(None,72)

        self.lifes = 3
        self.reset_game()

        self.heart = pygame.image.load('images\heart.png')

        self.speed_left_right = 75
        self.speed_car = 1
        self.speed_of_game = 0.00

        self.balance = 0

    def reset_game(self):
        self.lifes_left = self.lifes
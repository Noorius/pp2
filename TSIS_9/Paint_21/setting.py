import pygame

class Setting:
    def __init__(self):
        self.prev = None
        self.cur = None
        self.game_over = False

        self.back_color = 'WHITE'
        self.drawing_color = "BLACK"
        
        self.tool = None

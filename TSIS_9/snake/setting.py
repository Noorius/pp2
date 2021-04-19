import pygame

class Settings():
    def __init__(self):
        self.width = 600    #resolution
        self.height = 500   
        self.fps = 4        #game's speed
        self.font = pygame.font.SysFont('Comic',50) #game's font

        self.score = 0 #current score
        self.max_score = 0 # maximal got score for history
        
        
        self.game_on = False #start game
        self.levels = False #show levels
        self.edit = False #shows main menu

        self.block_size = 20 #size of walls, food, snake
        self.snake_color = (0,255,0) #current color of the snake
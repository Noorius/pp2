import pygame

class Snake():
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings
        self.speed = 1
        self.dx = 1
        self.dy = 0
        self.elements = []

        self.directions = {"D":True, "A":False, "W":True, 'S':True}

    def draw(self):
        for i in range(len(self.elements)):
            if i==0: #this is needed for collision with wall. I need rect of head only
                self.rect = pygame.draw.rect(self.screen,self.settings.snake_color,(self.elements[i][0],self.elements[i][1],20 - 2,20 - 2))
            pygame.draw.rect(self.screen,self.settings.snake_color,(self.elements[i][0],self.elements[i][1],20 - 2,20 - 2))
    
    def update(self):
        for i in range(len(self.elements) - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        
        if self.elements[0][0] < 0 or self.elements[0][0] > self.settings.width: #makes snake to appear at other side
            self.elements[0][0] %= self.settings.width
        if self.elements[0][1] < 0 or self.elements[0][1] > self.settings.height:
            self.elements[0][1] %= self.settings.height

        self.elements[0][0] += self.dx * 20 #I multiply to the size of block to make blocks be seen
        self.elements[0][1] += self.dy * 20
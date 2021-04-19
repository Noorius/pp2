import pygame

class Button:
    def __init__(self, screen, settings, width, height, text, pos: int):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.text = self.settings.font.render(text,True,(255,255,0))

        self.width = width
        self.height = height
        
        self.button_rect = pygame.Rect(250,100*pos,self.height,self.width)
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((0,0,255))

    def draw(self):
        self.screen.blit(self.surface,self.button_rect)
        self.screen.blit(self.text,(self.button_rect.x+5,self.button_rect.y+5))

import pygame.font

class Button:
    def __init__(self,screen, y):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 50, 50
        self.button_colour = (0, 255, 0)
        self.text_colour = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.left = self.screen_rect.left
        self.rect.y = y

        self.image = pygame.image.load(f'images/brush.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.rect.center

        

    def draw_button(self):
        self.screen.fill(self.button_colour,self.rect)
        self.screen.blit(self.image,self.image_rect)

import pygame
import random
from functions import *
from setting import Setting
from button import Button
from rectangle import Rectangle

pygame.init()

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
setting = Setting()

brush = Button(screen,100)
eraser = Button(screen,160)
eraser.image = pygame.image.load('images/eraser.png')
rectangle = Button(screen,220)
rectangle.image = pygame.image.load('images/rectangle.png')
circle = Button(screen,280)
circle.image = pygame.image.load('images/circle.png')
gen = Button(screen,340)
gen.image = pygame.image.load('images/gen.png')

buttons = [brush,eraser,rectangle,circle,gen]
colors = []
create_colors(colors,setting,screen)

screen.fill("WHITE")

while not setting.game_over:
    check_events(screen,setting,buttons,colors)
    
    for button in buttons:
      button.draw_button()

    for color in colors:
      color.show_me()

    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()

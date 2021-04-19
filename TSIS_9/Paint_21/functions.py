import pygame
from rectangle import Rectangle
from color import Color
from random import randint
from time import sleep
from datetime import datetime
import math

def check_events(screen,setting,buttons,colors):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            buttons.clear()
            colors.clear()
            setting.game_over = True
            path = datetime.now().strftime("%Y%m%d%H%M%S")
            pygame.image.save(screen,path+".png")

        if event.type == pygame.MOUSEBUTTONDOWN:
            setting.prev = event.pos

            check_buttons(setting,event.pos,buttons)

            if setting.tool == 4 and buttons[4].rect.collidepoint(event.pos):
                create_colors(colors,setting,screen)

            select_color(setting,colors,event.pos[0],event.pos[1])


        if event.type == pygame.MOUSEMOTION:
            setting.cur = pygame.mouse.get_pos()
            use_tool(screen,setting,colors)

        if event.type == pygame.MOUSEBUTTONUP:
            setting.prev = None

def check_buttons(setting,mouse_coor,buttons):
    for i in range(len(buttons)):
        if buttons[i].rect.collidepoint(mouse_coor):
            setting.tool = i

def use_tool(screen,setting,colors):
    if setting.prev and setting.tool == 0:
        pygame.draw.line(screen, setting.drawing_color, setting.prev, setting.cur, 3)
        setting.prev = setting.cur
    elif setting.prev and setting.tool == 1:
        pygame.draw.line(screen, setting.back_color, setting.prev, setting.cur, 10)
        setting.prev = setting.cur
    elif setting.prev and setting.tool == 2:
        rect = Rectangle(screen,setting) #drawing rectangle
        #sleep(1)
        rect.blitme()

    elif setting.prev and setting.tool == 3:
        center_x = setting.prev[0] + (setting.cur[0] - setting.prev[0])/2
        center_y = setting.prev[1] + (setting.cur[1] - setting.prev[1])/2
        radius = math.sqrt(pow((setting.cur[0]-center_x),2) + pow((setting.cur[1]-center_y),2))
        
        pygame.draw.circle(screen,setting.drawing_color,(center_x,center_y),radius,3)
        pygame.draw.circle(screen,setting.back_color,(center_x,center_y),radius-3)
        pygame.draw.circle(screen,setting.back_color,(center_x,center_y),radius+6,3)


def create_colors(colors,setting,screen):
    for i in range(7):
        x = 100 + i * 40 + i * 20
        color = Color(screen,x,0)
        color.fill = (randint(0,255),randint(0,255),randint(0,255))
        colors.append(color)

def select_color(setting,colors,mouse_x,mouse_y):
    for color in colors:
        if color.rect.collidepoint(mouse_x,mouse_y):
            setting.drawing_color = color.fill
        
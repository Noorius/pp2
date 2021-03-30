from point import Point
import sys
import pygame
import math

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_Q:
                sys.exit()

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope *    index    * dash_length)
        end   = origin + (slope * (index + 1) * dash_length)
        pygame.draw.line(surf, color, start.get(), end.get(), width)

def draw_lines(screen,color,start_pos, end_pos):
    #origin = Point(start_pos)
    #target = Point(end_pos)
    pygame.draw.line(screen,(0,255,0), (0,250), (1200,250), 1)
    pygame.draw.line(screen,(0,255,0), (628,0), (628,500), 1)
    for x in range(1200):
        y = math.sin(x/100) * -100 + 250
        pygame.draw.line(screen,color, (x,y), (x,y), 1)
        
    for x in range(0,1200,6):
        y1 = math.cos(x/100) * -100 + 250
        pygame.draw.line(screen,(0,0,255), (x,y1), (x,y1), 1)
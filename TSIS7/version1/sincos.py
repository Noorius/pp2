import pygame
import math
from functions import *

pygame.init()
screen = pygame.display.set_mode((1200,500))
done = False

while not done:
        check_event()
        #draw_dashed_line(screen,(0,255,0),(0,0),(110,110))
        draw_lines(screen,(255,0,0),(0,0),(110,110))
        pygame.display.flip()
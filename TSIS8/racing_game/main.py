import pygame
from setting import Settting
from functions import *
from car import Car
from pygame.sprite import Group

def run_game():
    pygame.init()
    pygame.mixer.music.load('sounds/track1.wav')
    pygame.mixer.music.play(-1)

    g_settings = Settting()
    screen = pygame.display.set_mode((g_settings.width,g_settings.height))
    pygame.display.set_caption("Racer 2D")

    car = Car(screen,g_settings)
    people = Group()
    coins = Group()
    hearts = Group()

    INC_SPEED = pygame.USEREVENT + 1 #event to increase speed
    COIN_APP = pygame.USEREVENT + 2 #event to coins' appearance
    HEART_APP = pygame.USEREVENT + 3 #event to hearts' appearance
    pygame.time.set_timer(INC_SPEED, 10000) #timer for 10 sec
    pygame.time.set_timer(COIN_APP,2000) #time for 50 sec
    pygame.time.set_timer(HEART_APP,15000)

    while True:
        check_events(car,people,coins,hearts,screen,g_settings,INC_SPEED,COIN_APP,HEART_APP)

        if g_settings.game_active:
            car.update()
            people.update()
            coins.update()
            hearts.update()
            update_people(people,screen,g_settings,car,coins,hearts)
            update_coins(coins,car,screen,g_settings)
            update_hearts(hearts,car,screen,g_settings)
            check_car(car,people,coins,hearts)
            

        update_screen(screen,g_settings,car,people,coins,hearts)
        
run_game()
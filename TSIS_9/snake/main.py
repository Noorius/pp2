import pygame
from pygame.sprite import Group
from snake import Snake
from food import Food
from setting import Settings
from button import Button
from functions import *


def run_game(): #runs game
    pygame.init() 
    pygame.display.set_caption("Snake 2021")
    snake_image = pygame.image.load('python.png') #loads image for main menu
    apple_tree = pygame.image.load('apple_tree.png')

    settings = Settings() #creates a setting object to control the game everywhere
    screen = pygame.display.set_mode((settings.width,settings.height))
    screen_rect = screen.get_rect()
    
    snake = Snake(screen,settings) #snake 1
    snake_2 = Snake(screen,settings) #snake 2
    snake_2.elements.append([200,200]) #adds one element because we don't save the 2nd snake

    food = Food(settings) #creates a food
    walls = [] #list of walls
    colors = [] #list of colors
    load_game(snake,food,settings) #loads the snake's, food's position and direction

    play_button = Button(screen, settings, 100, 50, "Play",1.5) #creates buttons
    setting_button = Button(screen, settings, 100, 50, "Edit",2.5)
    buttons = [play_button,setting_button]
    for i in range(1,4):
        buttons.append(Button(screen, settings, 120, 50, "Level "+str(i),i)) #adds three buttons for levels
    

    while True:
        check_events(screen,settings,snake,snake_2,food,buttons,walls,colors) #cheks for events
        
       
        settings.max_score_txt = settings.font.render('Max score '+str(settings.max_score),True,"BLUE")

        if not settings.game_on: #opens menu
            screen.fill("WHITE") 
            screen.blit(apple_tree,(-30,0))
            screen.blit(snake_image,(350,0))
            buttons[0].draw() #Play button
            buttons[1].draw() #Edit button
            pygame.draw.rect(screen,(255,255,255),(0,0,200,60))
            screen.blit(settings.max_score_txt,(0,20)) #shows max score all the time

        if settings.edit:
            pygame.draw.rect(screen,(255,255,255),(80,60,440,80)) #rectangle for better view
            for color in colors:
                color.show_me() #draws rectangles with colors

        if settings.levels: 
            screen.fill("WHITE")
            screen.blit(apple_tree,(-30,0))
            for i in range(2,len(buttons)):
                buttons[i].draw() #draws level buttons

        if settings.game_on:
            settings.score_txt = settings.font.render('Score '+str(settings.score),True,"BLUE")
            screen.fill('BLACK')

            snake.draw() #draws and updates snake's position on the screen
            snake.update()

            snake_2.draw() 
            snake_2.update()

            food.draw(screen) #draws food on screen

            for wall in walls: #draws walls on the screen
                wall.blit(screen)

            screen.blit(settings.score_txt,(0,20)) #shows current score on the screen

            iscollided(snake,food,settings) #check collision of snake and food
            check_game_over(snake,settings,walls) #check conditions for snake's loose

            iscollided(snake_2,food,settings)
            check_game_over(snake_2,settings,walls)

        pygame.display.flip()
        pygame.time.Clock().tick(settings.fps+len(snake.elements)) #speeds game by increasing fps

run_game()
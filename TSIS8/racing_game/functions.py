import pygame
import sys
from people import Human
from time import sleep
from coin import Coin
from heart import Heart

def check_keydown(event,car): #check for pressed button
    if event.key == pygame.K_d: #move right
        car.move_right = True
    elif event.key == pygame.K_a: #move left
        car.move_left = True
    elif event.key == pygame.K_w: #move up
        car.move_up = True
    elif event.key == pygame.K_s: #move down
        car.move_down = True
    elif event.key == pygame.K_SPACE:
        car.sound_beep.play()

def check_keyup(event,car): #check for released button
    if event.key == pygame.K_d: #stop move right
        car.move_right = False 
    elif event.key == pygame.K_a: #stop move left
        car.move_left = False
    elif event.key == pygame.K_w: #stop move up
        car.move_up = False
    elif event.key == pygame.K_s: #stop move down
        car.move_down = False
    elif event.key == pygame.K_SPACE:
        car.sound_beep.stop()

def check_events(car,people,coins,hearts,screen,g_settings,INC_SPEED,COIN_APP,HEART_APP): #check events

    for event in pygame.event.get(): #collects events in a queu of events
        if event.type == pygame.QUIT: #red cross is pressed
            sys.exit()
        elif event.type == pygame.KEYDOWN: #any button is pressed
            check_keydown(event,car)
        elif event.type == pygame.KEYUP: #any button is released
            check_keyup(event,car) 
        elif event.type == INC_SPEED: #event for game speed
            g_settings.speed_of_game += 0.1 #increases the speed increment 
        elif event.type == COIN_APP: #makes coins
            add_a_coin(coins,screen,g_settings)
        elif event.type == HEART_APP:
            add_a_heart(hearts,screen,g_settings)

def update_screen(screen,g_settings,car,people,coins,hearts): #uodates and draws objects 
    screen.fill(g_settings.back_colour) #fills the screen
    draw_lines(screen,g_settings) #draws lines
    car.blitme() #blits a car
    for coin in coins.sprites(): #blits every coin
        coin.blitme()
    for heart in hearts.sprites(): #blits every coin
        heart.blitme()
    for human in people.sprites(): #blits every human
        human.blitme()


    for i in range(g_settings.lifes_left+1): #displays lifes
        screen.blit(g_settings.heart,(i*64,0))

    text_life = g_settings.font.render(f"{round(float(2)+g_settings.speed_of_game,2)} km/h",True,'White')
    text_money = g_settings.font.render(f"{g_settings.balance} $",True,(255,255,51))
    screen.blit(text_life,(0,64)) #displays text
    screen.blit(text_money,(0,120))

    pygame.display.flip()

def draw_lines(screen,g_settings): #draws lines
    lines = g_settings.width // 75 #calculates how many lines for width
    for i in range(lines):
        pygame.draw.line(screen,(255,255,255),(75*i,0),(75*i,g_settings.height),3) #draws line one by one






def update_people(people,screen,g_settings,car,coins,hearts): #updates people
    if len(people)<5: #there should be no more than 5 people on the screen
        human = Human(screen,g_settings) 
        human.speed += g_settings.speed_of_game #add the current game's speed
        people.add(human) #adds to a group
    if pygame.sprite.spritecollideany(car,people): #checks for collisions betwwen car and people
        car_hitted(people,car,coins,hearts)
    remove_people(people) #check whether people out of borders
    check_people_collision(people) #checks whether two people overlap each other

def remove_people(people): #check whether people out of borders
    for human in people.sprites():
        if human.rect.top >= human.screen_rect.bottom: #if so, then removes them
            people.remove(human)

def check_people_collision(people):
    dictionary = pygame.sprite.groupcollide(people,people,False,False)
    for key, val in dictionary.items():
        key.speed = val[0].speed = min(key.speed,val[0].speed)
    dictionary.clear()





def car_hitted(people,car,coins,hearts): #the scenario for lose
    
    car.sound_crash.play() #plays souns of crash

    if car.g_settings.lifes_left > 0: #player's health should be non zero
        car.g_settings.lifes_left -= 1 #substract one life
        people.empty()
        coins.empty()
        hearts.empty() 
        car.center_car() 
        car.g_settings.speed_of_game = 0.00 #sets the initial speed of game
        sleep(1.5) #stop game for time to relax
        car.sound_revive.play() #sound of restart
    else:
        pygame.mixer.music.pause() #stops music
        car.g_settings.game_active = False #stops any activity, since no lifes

def check_car(car,people,coins,hearts): #this function check if a playes out of bourders
    if car.rect.top > car.screen_rect.bottom: 
        car_hitted(people,car,coins,hearts)
    
def update_coins(coins,car,screen,g_settings): 
    for coin in coins.sprites():
        if coin.rect.top >= coin.screen_rect.bottom: #if a coin out of the screen, then deletes it
            coins.remove(coin)

    if pygame.sprite.spritecollide(car,coins,True): #if a playes took a coin, then +1 to balance
        coin.sound.play()
        g_settings.balance += 1

def add_a_coin(coins,screen,g_settings): #create one coin
    #if len(coins)<10:
        coin = Coin(screen,g_settings)
        coin.speed += g_settings.speed_of_game #adds the current speed of a game
        coins.add(coin)

def add_a_heart(hearts,screen,g_settings):
    #if len(hearts)<1:
        heart = Heart(screen,g_settings)
        heart.speed += g_settings.speed_of_game #adds the current speed of a game
        hearts.add(heart)

def update_hearts(hearts,car,screen,g_settings): 
    for heart in hearts.sprites():
        if heart.rect.top >= heart.screen_rect.bottom: #if a coin out of the screen, then deletes it
            hearts.remove(heart)

    if pygame.sprite.spritecollide(car,hearts,True) and g_settings.lifes_left<3: #if a playes took a coin, then +1 to balance
        heart.sound.play()
        g_settings.lifes_left += 1


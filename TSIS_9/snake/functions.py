import pygame
from wall import Wall
from color import Color
from random import randint

def event_keydown(event,snake,snake_2): #direct snake 1 by keyboard pressing
    if event.key == pygame.K_d and snake.directions["D"]:
        snake.directions = {"D":False, "A":False, "W":True, 'S':True}
        snake.dx = snake.speed
        snake.dy = 0
    elif event.key == pygame.K_a and snake.directions["A"]:
        snake.directions = {"D":False, "A":False, "W":True, 'S':True}
        snake.dx = -snake.speed
        snake.dy = 0
    elif event.key == pygame.K_w and snake.directions["W"]:
        snake.directions = {"D":True, "A":True, "W":False, 'S':False}
        snake.dx = 0
        snake.dy = -snake.speed
    elif event.key == pygame.K_s and snake.directions["S"]:
        snake.directions = {"D":True, "A":True, "W":False, 'S':False}
        snake.dx = 0
        snake.dy = snake.speed

    #direct the second snake by keyboard pressing
    if event.key == pygame.K_RIGHT and snake_2.directions["D"]:
        snake_2.directions = {"D":False, "A":False, "W":True, 'S':True}
        snake_2.dx = snake_2.speed
        snake_2.dy = 0
    elif event.key == pygame.K_LEFT and snake_2.directions["A"]:
        snake_2.directions = {"D":False, "A":False, "W":True, 'S':True}
        snake_2.dx = -snake_2.speed
        snake_2.dy = 0
    elif event.key == pygame.K_UP and snake_2.directions["W"]:
        snake_2.directions = {"D":True, "A":True, "W":False, 'S':False}
        snake_2.dx = 0
        snake_2.dy = -snake_2.speed
    elif event.key == pygame.K_DOWN and snake_2.directions["S"]:
        snake_2.directions = {"D":True, "A":True, "W":False, 'S':False}
        snake_2.dx = 0
        snake_2.dy = snake_2.speed

def check_events(screen,settings,snake,snake_2,food,buttons,walls,colors): #checks events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game(snake,food,settings) #saves game before leaving
            exit()
        if event.type == pygame.KEYDOWN:
            event_keydown(event,snake,snake_2)
        if event.type == pygame.MOUSEBUTTONDOWN and not settings.game_on:
            mouse_x, mouse_y = pygame.mouse.get_pos() #gets cirrent position
            for i in range(len(buttons)): 
                if check_button_pressed(buttons[i],mouse_x,mouse_y): #cheks all buttons in buttons list for pressing
                    button_pressed(screen,settings,walls,buttons,colors,i) #each scenario for each button
            select_color(settings,colors,mouse_x,mouse_y) #checks pressing to color squares

def iscollided(snake,food,settings):
    if snake.elements[0][0]==food.x and snake.elements[0][1]==food.y: #when snake's and food's coordinates are the same
        snake.elements.append([-100,-100]) #add a body part
        food.new_coor() #make a new coordinates for food
        settings.score += 5 #add 5 to current score
        settings.fps += 1 #increase game speed

def check_button_pressed(button,mouse_x,mouse_y):
    xcoor = button.button_rect.x #gets button x-coor
    ycoor = button.button_rect.y #gets button y-coor
    if mouse_x in range(xcoor, xcoor + button.width) and mouse_y in range(ycoor, ycoor + button.height):
        return True #checks whether mouse's coor in range of buttons, return bool
    
def button_pressed(screen,settings,walls,buttons,colors,i):
    if i == 0:
        settings.levels = True #if play button pressed, then show level menu
    elif i == 1:
        create_colors(colors,settings,screen) #if edit button is pressed, then show colors
        settings.edit = True
    elif settings.levels: #other buttons are for levels
        draw_levels(settings,walls,i) #draw level depending of button's number
        settings.game_on = True #starts game
        settings.levels = False #closes level menu
        
def draw_levels(settings,walls,i): # 2,3,4 indexes for 1,2,3
    if i>2: # 3 and 4 are greater than 2
        for k in range(0,settings.height,20):
            create_wall(walls,0,k)
            create_wall(walls,settings.width - 20,k)
    if i%2==0: # 2 and 4 are even
        for k in range(0,settings.width,20):
            create_wall(walls,k,0)
            create_wall(walls,k,settings.height - 20)

def create_wall(walls,x,y):#creates one wall object by given coordinates
    wall = Wall() 
    wall.rect.x = x
    wall.rect.y = y
    walls.append(wall)

def create_colors(colors,setting,screen): #add colors to colors list if called
    for i in range(7):
        x = 100 + i * 40 + i * 20
        color = Color(screen,x,80)
        color.fill = (randint(0,255),randint(0,255),randint(0,255))
        color.surface.fill(color.fill)
        colors.append(color)

def select_color(settings,colors,mouse_x,mouse_y): #checks pressing at any color button
    for color in colors:
        if color.rect.collidepoint(mouse_x,mouse_y):
            settings.snake_color = color.fill

def check_game_over(snake,settings,walls): #game over if snake collides with wall or eats itself
    sn_x = snake.elements[0][0]
    sn_y = snake.elements[0][1]
    for wall in walls:
        if pygame.Rect.colliderect(snake.rect,wall.rect) or eating_myself(snake):
            walls.clear() #clear walls for this level
            settings.game_on = False #stop game
            snake.elements = [[100,100]] #snake starts with 1 element
            if settings.score > settings.max_score: settings.max_score = settings.score #update max_score if bigger

def eating_myself(snake):
    body = snake.elements[1:len(snake.elements)-1]
    if snake.elements[0] in body: #if head coordines in body coor, then snake eat itself
        return True 

def save_game(snake,food,settings): #saves elements, food coor, score and direction to txt file
    if settings.score > settings.max_score: settings.max_score = settings.score
    with open('save.txt','w') as f:
        for element in snake.elements:
            f.write(str(element[0])+" "+str(element[1])+" ")
        f.write('\n'+str(food.x)+' '+str(food.y)+'\n'+str(settings.score))
        f.write('\n'+str(snake.dx)+" "+str(snake.dy))

    with open('max_score.txt','a') as f:
        f.write(" "+str(settings.max_score))
 
def load_game(snake,food,settings): #imports everything to the game
    with open('save.txt','r') as f:
        save = f.readlines()
        list_body = save[0].split()
        for i in range(0,len(list_body)-1,2):
            snake.elements.append([int(list_body[i]),int(list_body[i+1])])
        food_coor = save[1].split()
        food.x,food.y = int(food_coor[0]),int(food_coor[1])
        settings.score = int(save[2])
        snake.dx = int(save[3].split()[0])
        snake.dy = int(save[3].split()[1])
    
    with open('max_score.txt','r') as f:
        list = f.readline().split()
        settings.max_score = int(max(list))



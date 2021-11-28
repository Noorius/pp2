import pygame
import sys
import os
from object import Object
from products import Product
from random import choice
from random import randint
from time import sleep

def keydown_events(event,cather,g_setting):
    if event.key == pygame.K_a:
        g_setting.move_left = True
    elif event.key == pygame.K_d:
        g_setting.move_right = True
    elif event.key == pygame.K_SPACE:
        cather.open_mouth = True

def keyup_events(event,catcher,g_setting):
    if event.key == pygame.K_a:
        g_setting.move_left = False
    elif event.key == pygame.K_d:
        g_setting.move_right = False
    elif event.key == pygame.K_SPACE:
        catcher.open_mouth = False

def check_event(catcher,g_setting):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event,catcher,g_setting)
        elif event.type == pygame.KEYUP:
            keyup_events(event,catcher,g_setting)

def update_screen(screen,catcher,objects,products,g_setting,stats):
    screen.blit(g_setting.background,catcher.screen_rect)
    for objecti in objects.sprites():
        objecti.blitme()
    for product in products.sprites():
        product.blitme()
    catcher.blitme()
    update_text(screen,catcher,g_setting,stats)

def update_objects(objects,screen,g_setting,catcher):
    if len(objects) < g_setting.allowed_drops:
        object_create(objects,screen,g_setting)
    for objecti in objects.copy():
        if objecti.rect.top >= objecti.screen_rect.bottom:
            objects.remove(objecti)

def update_products(products,screen,g_setting,catcher):
    if len(products) < g_setting.allowed_drops:
        products_create(products,screen,g_setting)
    for product in products.copy():
        if product.rect.top >= product.screen_rect.bottom:
            products.remove(product)

def check_collision(catcher,objects,products,stats,g_setting):
    if catcher.health <= 0:
        no_health(catcher,objects,products,stats,g_setting)
    objecti = pygame.sprite.spritecollideany(catcher,objects)
    product = pygame.sprite.spritecollideany(catcher,products)
    if objecti:
        if catcher.open_mouth:
            catcher.health -= 10  
        else:
            catcher.health -= 5
        objecti.kill()
    elif product:
        if catcher.open_mouth and catcher.health < 100: 
            catcher.health += 10
            product.kill()


def object_create(objects,screen,g_setting):
    objecti = Object(screen,g_setting)
    list_of_trash=os.listdir("images/trash")
    objecti.image = pygame.image.load("images/trash/"+f"{choice(list_of_trash)}")
    objects.add(objecti)

def products_create(products,screen,g_setting):
    product = Product(screen,g_setting)
    list_of_food = os.listdir("images/food")
    product.image = pygame.image.load("images/food/"+f"{choice(list_of_food)}")
    products.add(product)

def update_text(screen,catcher,g_setting,stats):
    health = g_setting.font.render("Health: {0} Lifes: {1}".format(int(catcher.health),stats.life_left),True,(251, 255, 0))
    screen.blit(health,(10,10))

def no_health(catcher,objects,products,stats,g_setting):

    if stats.life_left == 0:
        g_setting.game_active = False
    else:
        stats.life_left -= 1

        objects.empty()
        products.empty()

        catcher.center_catcher()
        catcher.health = 100

        sleep(0.5)
    


    

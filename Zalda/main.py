#Zalda Zelda like killing things game Copyright 2013, Collin Norwood
import pygame, sys, math, random
from map_1 import map1

#Set up variables
pygame.init()
screen = pygame.display.set_mode([1680,1000])
right = False
left = False
up = False
down = False
lnkx = 0
lnky = 0

linked = pygame.image.load("img/linked.png")

black = pygame.image.load("img/black.jpg")
dirt = pygame.image.load("img/dirt.jpg")
grass = pygame.image.load("img/grass.jpg")
water = pygame.image.load("img/water.jpg")
mountian = pygame.image.load("img/mountian.jpg")

terrains = [{"sprite": black}, {"sprite": dirt}, {"sprite": grass}, {"sprite": water}, {"sprite": mountian}]

themap = [[-1 for y in range(150)] for x in range (150)]

for x in range (0,150):
    for y in range (0,150):
        themap[y][x] = terrains[map1[y][x]]

#game loop
while True:                                
    pygame.time.delay(20)       
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()        
        elif event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False            
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False            
    
    if right == True:            
        lnkx = lnkx + 16
    if left == True:            
        lnkx = lnkx - 16
    if up == True:            
        lnky = lnky - 16
    if down == True:            
        lnky = lnky + 16
    
    #blitting stuff            
    for x in range (0, 150):
        for y in range (0, 150):
            screen.blit(themap[y][x]["sprite"], [x * 16, y * 16])
    
    screen.blit(linked, [lnkx, lnky])
    
    pygame.display.flip()

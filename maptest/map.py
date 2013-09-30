import pygame, sys, math, random
pygame.init()
screen = pygame.display.set_mode([1680,1000])
dirt = pygame.image.load("dirt.jpg")
mountian = pygame.image.load("mountian.jpg")
water = pygame.image.load("water.jpg")

terrains = [{"sprite": dirt}, {"sprite": mountian}, {"sprite": water}]

themap = [[-1 for x in range(150)] for y in range (150)]

for x in range (0,150):
    for y in range (0,150):
        themap[x][y] = terrains[random.randint(0,2)]

while True:                                
    pygame.time.delay(50)   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for x in range (0,150):
                    for y in range (0,150):
                        themap[x][y] = terrains[random.randint(0,2)]

    for x in range (0, 150):
        for y in range (0, 150):
            screen.blit(themap[x][y]["sprite"], [x * 16, y * 16])
    
    
    pygame.display.flip()

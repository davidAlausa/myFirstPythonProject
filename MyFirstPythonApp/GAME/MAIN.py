import pygame
from Config import *
from introScreen import introScreen

#initialising PYGAME
pygame.init()
clock = pygame.time.Clock()

#opening WINDOW
displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('MonsterHotel')

#initialising VARIABLES
intrscrn = introScreen(displaySurface)
isGameRunning = True
gmPHASE = 'I'

#LOOP
while isGameRunning:
    #handling QUITS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isGameRunning = False
    
    #deciding GAME'S PHASE
    if gmPHASE == 'I':
        intrscrn.run()

        
    #refreshing DISPLAY
    pygame.display.flip()
    clock.tick(60)

#closing GAME
pygame.quit()

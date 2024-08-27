import pygame
import moviepy.editor
from Config import *
from introScreen import introScreen
from elevatorScreen import elevatorScreen

#initialising PYGAME
pygame.init()
clock = pygame.time.Clock()

#opening WINDOW
displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('MonsterHotel')

#initialising VARIABLES
intrscrn = introScreen(displaySurface)
elvtrscrn = elevatorScreen(displaySurface)
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
        gmPHASE = intrscrn.run()
    elif gmPHASE == 'P':
        video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'is_to_hs.mov')
        video.preview()
        gmPHASE = elvtrscrn.run()
    #refreshing DISPLAY
    pygame.display.flip()
    clock.tick(60)

#closing GAME
pygame.quit()


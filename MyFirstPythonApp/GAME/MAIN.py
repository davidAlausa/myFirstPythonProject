import pygame
import moviepy.editor 
from moviepy.video.fx.all import resize
from Config import *
from introScreen import introScreen
from elevatorScreen import elevatorScreen
from FUNCTIONALITY import Game

#initialising PYGAME
pygame.init()
clock = pygame.time.Clock()

#opening WINDOW
displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('MonsterHotel')

#initialising VARIABLES
game = Game()
intrscrn = introScreen(displaySurface)
elvtrscrn = elevatorScreen(displaySurface,game)
isGameRunning = True
gmPHASE = 'I'
video_played = False
flrprssd = (False,1,1)

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
        # if not video_played:
        #     video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'is_to_hs.mp4', audio= False)
        #     video.preview()
        #     video_played = True

        flrprssd = elvtrscrn.run()
        if flrprssd[0] == True:
            current = flrprssd[2].hotel.getFloor()
            video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'e_BACKGROUND_DOORSCLOSE.mp4', audio= False)
            video.preview()

            while current != flrprssd[1]:
                video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'e_Countdown_'+str(current)+'_resized.mp4', audio= False)
                video.preview() 
                if current > flrprssd[1]:
                    current = current-1
                else:
                    current = current+1
            video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'e_Countdown_'+str(current)+'_resized.mp4', audio= False)
            video.preview()
            
            video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'e_BACKGROUND_DOORSOPEN_resized.mp4', audio= False)
            video.preview()



    #refreshing DISPLAY
    pygame.display.flip()
    clock.tick(60)

#closing GAME
pygame.quit()


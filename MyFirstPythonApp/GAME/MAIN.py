import pygame
import moviepy.editor 
from Config import *
from introScreen import introScreen
from elevatorScreen import elevatorScreen
from FUNCTIONALITY import Game
from event import event
from monsterScreen import monsterScreen

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
mnstrscrn = monsterScreen(displaySurface, game)   
isGameRunning = True
gmPHASE = 'I'
video_played = False
flrprssd = (False,1,1)
evnt = event(game, displaySurface)

#print('THE MONSTER IS ON FLOOR:'+str(game.getMonsterFloorLevel())+' \tTHE KEY IS ON FLOOR:' + str(game.getKeyFloorLevel()))
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
        if not video_played:
            video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'is_to_hs.mp4', audio= False)
            video.preview()
            video_played = True
        flrprssd = elvtrscrn.run()
        if flrprssd[0] == True:
            current = flrprssd[2].hotel.getFloor()
            video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'e_BACKGROUND_DOORSCLOSE.mp4', audio= False)
            video.preview()

            while current != flrprssd[1]:
                video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'e_Countdown_'+str(current)+'.mp4', audio= False)
                video.preview() 
                if current > flrprssd[1]:
                    current = current-1
                else:
                    current = current+1
            
            newfloorlevel = flrprssd[1] 

            game.setHotelFloor(newfloorlevel)
            video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'e_Countdown_'+str(current)+'.mp4', audio= False)
            video.preview()
            
            video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'e_BACKGROUND_DOORSOPEN.mp4', audio= False)
            video.preview()

            if game.checkEndGameStatus():
                print('YOU REACHED THE END OF THE GAME!!! YOU ENDED WITH:' +str(game.getPlayerLives()) + ' lives and ' +str(game.getKeyInventoryCount())+ ' keys')
                isGameRunning = False

            else:
                gmPHASE = evnt.checkElevatorChoice(newfloorlevel)

    elif gmPHASE == 'M':
        isEventOver = mnstrscrn.run()

        if isEventOver[0]:
            if isEventOver [1]:
                video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'me_MONSTERWINS.mp4', audio= False)
                video.preview()
                isGameRunning = False
            elif isEventOver [2]:
                video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'me_MONSTERDEFEATED.mp4', audio= False)
                video.preview()
                game.resetMonster()
                gmPHASE = 'P'



    #refreshing DISPLAY
    pygame.display.flip()
    clock.tick(60)

#closing GAME
pygame.quit()   


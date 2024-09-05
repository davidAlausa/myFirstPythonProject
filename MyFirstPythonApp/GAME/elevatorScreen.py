import pygame
from Config import *
from elevatorScreenBACKGROUND import elevatorScreenBACKGROUND
from elevatorScreenGAMESTATUS import elevatorScreenGAMESTATUS
from FUNCTIONALITY import Game
import moviepy.editor 

class elevatorScreen():
    def __init__(self,displaySurface,GAME):
        #initialising BACKGROUNDS
        self.elevatorScreenBackground = elevatorScreenBACKGROUND((413,280,10,10),(413,260,10,10),(413,243,10,10),(413,225,10,10),(413,208,10,10))
        self.elevatorScreenGAMESTATUS = elevatorScreenGAMESTATUS()

        #use this to draw to WINDOW
        self.displaySurface = displaySurface
        #using this to check if TAB is being held down
        self.showGameStatus = False

        self.game = GAME


    #updates SPRITES
    def update(self):
        floorPRESSED = self.elevatorScreenBackground.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            self.showGameStatus = True
        else:
            self.showGameStatus = False
        
        if self.game.validateElevatorFloor(floorPRESSED):            
            return (True, floorPRESSED,self.game)
        else:
            if self.game.isSameFloorPressed:
                video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'e_BACKGROUND_SAMEFLOOR.mp4', audio= False)
                video.preview()
            return (False, floorPRESSED,self.game)
        
    #draws LEVEL to screen
    def draw(self):
        self.elevatorScreenBackground.draw(self.displaySurface)
        if self.showGameStatus:
            self.elevatorScreenGAMESTATUS.draw(self.displaySurface, self.game.getKeyInventoryCount(), self.game.getPlayerLives(), self.game.hotel.getFloor())
    
    #will be called fom GAME loop
    def run(self):
        isfloorpressed = self.update()
        self.draw()
        return isfloorpressed

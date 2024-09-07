import pygame
from Config import *
import moviepy.editor 
from FUNCTIONALITY import Game
import random
from monsterScreen import monsterScreen

class event():

    def __init__(self, game, displaysurface):

        self.game = game
        self.displaysurface = displaysurface

    
    def checkElevatorChoice(self, choice):

        if choice == self.game.getMonsterFloorLevel():  
            self.monsterEvent()
            return 'M'
        
        elif choice == self.game.getKeyFloorLevel():
            if self.game.getKeyInventoryCount()!=3:
                self.keyFound()
                return'P'
            else:
                self.emptyFloor()
                return 'P'
        
        else:
            if choice !=1:
                self.emptyFloor()
            else:
                video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'f_GROUND.mp4', audio= False)
                video.preview()
            return 'P'


    def emptyFloor(self):
        event = random.randint(1,5)
        
        video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'f_NOTHING_'+ str(event) +'.mp4', audio= False)
        video.preview()

        if event==5:
            if self.game.getPlayerLives() != 3:
                self.game.setPlayerLives(self.game.getPlayerLives()+ 1)

    def keyFound(self):
        video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'K_KEYFOUND.mp4', audio= False)
        video.preview()
        self.game.keyFound()


    def monsterEvent(self):
        video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'me_MONSTERINTRO.mp4', audio= False)
        video.preview()
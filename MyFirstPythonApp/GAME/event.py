import pygame
from Config import *
import moviepy.editor 
from FUNCTIONALITY import Game
import random

class event():

    def __init__(self, game):

        self.game = game   

    
    def checkElevatorChoice(self, choice):

        if choice == self.game.getMonsterFloorLevel():  
            self.monsterEvent()
        
        elif choice == self.game.getKeyFloorLevel():
            if self.game.getKeyInventoryCount()!=3:
                self.keyFound()
            else:
                self.emptyFloor()
        
        else:
            self.emptyFloor()


    def emptyFloor(self):
        event = random.randint(1,5)
        
        video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'f_NOTHING_'+ str(event) +'.mp4', audio= False)
        video.preview()

    def keyFound(self):
        video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'K_KEYFOUND.mp4', audio= False)
        video.preview()
        self.game.keyFound()


    def monsterEvent(self):
        print('LOOOLL YOU ENCOUNTERED THE MONSTER BUT THIS FUNCTIONALITY ISNT IMPLEMENTED YET')
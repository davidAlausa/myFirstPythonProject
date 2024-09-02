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
           self.keyFound()
        
        else:
            self.emptyFloor()

    def emptyFloor(self):
        event = random.randint(1,5)
        
        video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'f_NOTHING_'+ str(event) +'_resized.mp4', audio= False)
        video.preview()

    def keyFound(self):
        print('LOOOLL THE KEY WAS FOUND BUT THIS FUNCTIONALITY ISNT IMPLEMENTED YET')

    def monsterEvent(self):
        print('LOOOLL YOU ENCOUNTERED BUT THIS FUNCTIONALITY ISNT IMPLEMENTED YET')
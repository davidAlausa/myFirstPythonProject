import pygame
from Config import *
from elevatorScreenBACKGROUND import elevatorScreenBACKGROUND


class elevatorScreen():
    def __init__(self,displaySurface):
        #initialising BACKGROUNDS
        self.elevatorScreenBackground = elevatorScreenBACKGROUND()
        #use this to draw to WINDOW
        self.displaySurface = displaySurface

    #updates SPRITES
    def update(self):
        pass
    
    #draws LEVEL to screen
    def draw(self):
        self.elevatorScreenBackground.draw(self.displaySurface)
    
    #will be called fom GAME loop
    def run(self):
        self.update()
        self.draw()

import pygame
from Config import *
from introScreenBACKGROUND import introScreenBackground
from introScreenNEWGAME import introScreenNEWGAME


class introScreen():
    def __init__(self,displaySurface):#
        #initialising BACKGROUNDS
        self.introScreenBackground = introScreenBackground()
        self.introScreenNEWGAME = introScreenNEWGAME((175,350),moveHover = True)
        #use this to draw to WINDOW
        self.displaySurface = displaySurface

    #updates SPRITES
    def update(self):
        self.introScreenNEWGAME.update(self)
    
    #draws LEVEL to screen
    def draw(self):
        self.introScreenBackground.draw(self.displaySurface)
        self.introScreenNEWGAME.draw(self.displaySurface)
    
    #will be called fom GAME loop
    def run(self):
        self.update()
        self.draw()

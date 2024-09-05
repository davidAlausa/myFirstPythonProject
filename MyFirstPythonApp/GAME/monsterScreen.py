import pygame
from Config import *
from FUNCTIONALITY import Game
from monsterScreenBACKGROUND import monsterScreenBACKGROUND


class monsterScreen():
    def __init__(self, displaySurface, Game):
        self.monsterEventBACKGROUND = monsterScreenBACKGROUND(Game)
        self.displaysurface = displaySurface
    
    def draw(self):
        isEventOver = self.monsterEventBACKGROUND.run(self.displaysurface)
        return isEventOver
    
    def run (self):
        isEventOver = self.draw()
        return isEventOver

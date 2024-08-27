import pygame
from Config import *


class elevatorScreenBACKGROUND():
    def __init__(self):

        #initialising and resizing BACKGROUND 
        self.elevatorscreen_BACKGROUND = pygame.image.load(SPRITESHEET_PATH + 'e_BACKGROUND.jpg').convert()
        self.elevatorscreen_BACKGROUND = pygame.transform.scale(self.elevatorscreen_BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))


    def draw(self, displaySurface):
        displaySurface.blit(self.elevatorscreen_BACKGROUND, (0,0))
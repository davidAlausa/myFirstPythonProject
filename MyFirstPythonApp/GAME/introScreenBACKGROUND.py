import pygame
from Config import *


class introScreenBackground():
    def __init__(self):

        #initialising and resizing BACKGROUND 
        self.introscreen_BACKGROUND = pygame.image.load(SPRITESHEET_PATH + 'is_BACKGRUND.webp').convert()
        self.introscreen_BACKGROUND = pygame.transform.scale(self.introscreen_BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))


    def draw(self, displaySurface):
        displaySurface.blit(self.introscreen_BACKGROUND, (0,0))
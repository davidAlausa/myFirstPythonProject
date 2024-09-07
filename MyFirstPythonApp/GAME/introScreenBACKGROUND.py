import pygame
from Config import *


class introScreenBackground():
    def __init__(self):
        #initialising and resizing BACKGROUND 
        self.introscreen_BACKGROUND = pygame.image.load(SPRITESHEET_PATH + 'is_BACKGRUND.webp').convert()
        self.introscreen_BACKGROUND = pygame.transform.scale(self.introscreen_BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.INSTRUCTIONS_NOTSELECTED = pygame.image.load(SPRITESHEET_PATH + 'is_INSTRUCTIONS_NOTSELECTED.png').convert_alpha()
        self.INSTRUCTIONS_NOTSELECTED = pygame.transform.scale(self.INSTRUCTIONS_NOTSELECTED, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.INSTRUCTIONS_SELECTED = pygame.image.load(SPRITESHEET_PATH + 'is_INSTRUCTIONS_SELECTED.png').convert_alpha()
        self.INSTRUCTIONS_SELECTED = pygame.transform.scale(self.INSTRUCTIONS_SELECTED, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.INSTRUCTIONS = self.INSTRUCTIONS_NOTSELECTED

       # self.INSTRUCTIONSIMAGE = self.INSTRUCTIONS.subsurface(pygame.Rect(150,435,390,485))
        self.INSTRUCTIONSIMAGE = self.INSTRUCTIONS.subsurface(pygame.Rect(0,0,540,540))
        self.INSTRUCTIONSRECT = self.INSTRUCTIONSIMAGE.get_rect(center = (240,240))

        self.hoverArea = pygame.Rect(150,435,390 - 150, 485 - 435)#tlwh


    def update(self):

        if self.hoverArea.collidepoint(pygame.mouse.get_pos()):
            self.INSTRUCTIONS = self.INSTRUCTIONS_SELECTED
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            self.INSTRUCTIONS = self.INSTRUCTIONS_NOTSELECTED
            return False

    def draw(self, displaySurface):
        displaySurface.blit(self.introscreen_BACKGROUND, (0,0))
        displaySurface.blit(self.INSTRUCTIONS, (0,0))
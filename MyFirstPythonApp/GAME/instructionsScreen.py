import pygame
from Config import *
import time



class instructionsScreen():
    def __init__(self,displaySurface):
        #initialising BACKGROUNDS
        self.instructionscreen_1 = pygame.image.load(SPRITESHEET_PATH + 'is_INSTRUCTIONSPAGE_1.png').convert()
        self.instructionscreen_2 = pygame.image.load(SPRITESHEET_PATH + 'is_INSTRUCTIONSPAGE_2.png').convert()
        self.instructionscreen_3 = pygame.image.load(SPRITESHEET_PATH + 'is_INSTRUCTIONSPAGE_3.png').convert()
        self.instructionscreen_4 = pygame.image.load(SPRITESHEET_PATH + 'is_INSTRUCTIONSPAGE_4.png').convert()
        self.instructionscreen_5 = pygame.image.load(SPRITESHEET_PATH + 'is_INSTRUCTIONSPAGE_5.png').convert()

        self.instructionscreen_1 = pygame.transform.scale(self.instructionscreen_1, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.instructionscreen_2 = pygame.transform.scale(self.instructionscreen_2, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.instructionscreen_3 = pygame.transform.scale(self.instructionscreen_3, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.instructionscreen_4 = pygame.transform.scale(self.instructionscreen_4, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.instructionscreen_5 = pygame.transform.scale(self.instructionscreen_5, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.currentscreenpage = (
            self.instructionscreen_1,
            self.instructionscreen_2,
            self.instructionscreen_3,
            self.instructionscreen_4,
            self.instructionscreen_5
        )

        self.currentpage = 0

        self.forwardcoods = pygame.Rect(412, 435, 483 - 400, 479 - 435)
        self.backwardcoods = pygame.Rect(57, 423, 114 - 45, 475 - 423)
    #updates SPRITES
    def update(self):
        if self.forwardcoods.collidepoint(pygame.mouse.get_pos()) and self.currentpage != 4:
            if pygame.mouse.get_pressed()[0]:
                self.currentpage = self.currentpage + 1
        elif self.backwardcoods.collidepoint(pygame.mouse.get_pos()) and self.currentpage != 0:
            if pygame.mouse.get_pressed()[0]:
                self.currentpage = self.currentpage - 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return 'I'
        else:
            return 'INS'

    
    #draws LEVEL to screen
    def draw(self, displaySurface):
        displaySurface.blit(self.currentscreenpage[self.currentpage], (0,0))
 
    #will be called fom GAME loop
    def run(self,displaySurface):
        GAME_PHASE = self.update()
        self.draw(displaySurface)
        time.sleep(0.1)
        return GAME_PHASE

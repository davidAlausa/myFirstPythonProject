import pygame
from Config import *


class introScreenNEWGAME():
    def __init__(self, position, moveHover):

        #initialising and resizing NEWGAME
        introscreen_NEWGAME = pygame.image.load(SPRITESHEET_PATH + 'is_NEWGAMETXT.png').convert_alpha()
        introscreen_NEWGAME = pygame.transform.scale(introscreen_NEWGAME, (200,200))
        self.image = introscreen_NEWGAME.subsurface(pygame.Rect(0,0,200,200))
        self.rect = self.image.get_rect(bottomleft = position)
        self.movingHover = moveHover
        
    def update(self,introscreen):
        if self.movingHover == False:
            self.rect.y -=SPEED_NEWGAME # UP
        else:
            self.rect.y +=SPEED_NEWGAME # DOWN

        if self.rect.top < 160:
            self.movingHover =True
        if self.rect.bottom > 370:
            self.movingHover = False 

    def draw(self,displaySurface):
        displaySurface.blit(self.image, self.rect)
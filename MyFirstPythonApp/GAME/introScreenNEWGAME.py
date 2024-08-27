import pygame
from Config import *


class introScreenNEWGAME():
    def __init__(self, position, moveHover):

        #initialising and resizing NEWGAME
        introscreen_NEWGAME = pygame.image.load(SPRITESHEET_PATH + 'is_NEWGAMETXT.png').convert_alpha()
        introscreen_NEWGAME = pygame.transform.scale(introscreen_NEWGAME, (200,200))
        
        introscreen_NEWGAME_SELECTED = pygame.image.load(SPRITESHEET_PATH + 'is_NEWGAMETXT_SELECTED.png').convert_alpha()
        introscreen_NEWGAME_SELECTED = pygame.transform.scale(introscreen_NEWGAME_SELECTED, (200,200))

        self.image_NOTSELECTED = introscreen_NEWGAME.subsurface(pygame.Rect(0,0,200,200))
        self.image = self.image_NOTSELECTED
        self.rect = self.image.get_rect(bottomleft = position)
        
        self.image_SELECTED = introscreen_NEWGAME_SELECTED.subsurface(pygame.Rect(0,0,200,200))
        self.rect_SELECTED = self.image_SELECTED.get_rect(bottomleft = position)


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

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.image_SELECTED
            self.rect.x, self.rect.y = 175,170
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            self.image = self.image_NOTSELECTED
            return False
        
    def draw(self,displaySurface):
        displaySurface.blit(self.image, self.rect)
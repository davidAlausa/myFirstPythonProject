import pygame, sys
from pygame.locals import *
from Config import *
from FUNCTIONALITY import Game
import random
import moviepy.editor 

class monsterScreenATTACKBOARD():
    def __init__(self, game):
        self.monsterEvent_ATTACKBOARD_HI1 = pygame.image.load(SPRITESHEET_PATH + 'me_HARMFULITEM_1.png').convert_alpha()
        self.monsterEvent_ATTACKBOARD_HI2 = pygame.image.load(SPRITESHEET_PATH + 'me_HARMFULITEM_2.png').convert_alpha()
        self.monsterEvent_ATTACKBOARD_HI3 = pygame.image.load(SPRITESHEET_PATH + 'me_HARMFULITEM_3.png').convert_alpha()
        self.monsterEvent_ATTACKBOARD_AI = pygame.image.load(SPRITESHEET_PATH + 'me_ATTACKITEM.png').convert_alpha()
        self.monsterEvent_ATTACKBOARD_P1 = pygame.image.load(SPRITESHEET_PATH + 'me_PLAYER.png').convert_alpha()
        
        self.monsterEvent_ATTACKBOARD_HIARRAY = (
            self.monsterEvent_ATTACKBOARD_HI1,
            self.monsterEvent_ATTACKBOARD_HI2,
            self.monsterEvent_ATTACKBOARD_HI3
        )
        self.monsterEvent_ATTACKBOARD_HI = self.monsterEvent_ATTACKBOARD_HIARRAY[random.randint(0,2)]

        self.imageHI = self.monsterEvent_ATTACKBOARD_HI.subsurface(pygame.Rect(0,0,50,50))
        self.imageAI = self.monsterEvent_ATTACKBOARD_AI.subsurface(pygame.Rect(0,0,50,50))
        self.imageP1 = self.monsterEvent_ATTACKBOARD_P1.subsurface(pygame.Rect(0,0,50,50))

        self.oovPosition = (120,335)
        self.P1InitialPosition = (235,460)

        self.rectHI = self.imageHI.get_rect(bottomleft = self.oovPosition)
        self.rectAI = self.imageAI.get_rect(bottomleft = self.oovPosition)
        self.rectP1 = self.imageP1.get_rect(bottomleft = self.P1InitialPosition)

        self.ItemThrown = False
        self.ItemVelocity = [0, 0]
        self.isHarmful = False

        self.game = game

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rectP1.top > 335:
            if pressed_keys[K_UP]:
                self.rectP1.move_ip(0,-5)
        if self.rectP1.bottom < 525:
            if pressed_keys[K_DOWN]:
                self.rectP1.move_ip(0,5)
        if self.rectP1.left > 120:
              if pressed_keys[K_LEFT]:
                  self.rectP1.move_ip(-5, 0)
        if self.rectP1.right < 410:        
              if pressed_keys[K_RIGHT]:
                  self.rectP1.move_ip(5, 0)

        if not self.ItemThrown:
            harmfulorHelpful = random.randint(1,10)
            if harmfulorHelpful < 8:
                self.createItem(self.rectHI, self.imageHI)
                self.isHarmful = True
            else:
                self.createItem(self.rectAI, self.imageAI)
                self.isHarmful = False
        if self.isHarmful:
            self.move(self.rectHI, self.imageHI)
        else:
            self.move(self.rectAI, self.imageAI)

        isEventOver = self.didCollide()
        return isEventOver

    def createItem(self, rect, image):
        pick = random.randint(1, 4)
        self.ItemThrown = True 
        if pick == 1:
            rect.centerx = random.randint(120, 390)
            rect.centery = 335
            self.ItemVelocity = [random.choice([-2, -1, 1, 2]), random.choice([-2, -1, 1, 2])]
        elif pick == 2:
            rect.centerx = random.randint(120, 390)
            rect.centery = 505
            self.ItemVelocity = [random.choice([-2, -1, 1, 2]), random.choice([-2, -1, 1, 2])]
        elif pick == 3:
            rect.centerx = 120
            rect.centery =  random.randint(335, 505)
            self.ItemVelocity = [random.choice([1, 2]), random.choice([-2, -1, 1, 2])]
        elif pick == 4:
            rect.centerx = 390
            rect.centery =  random.randint(335, 505)
            self.ItemVelocity = [random.choice([-2, -1]), random.choice([-2, -1, 1, 2])]
                                            
                                
    def didCollide (self):
        smallerRectHI = self.rectHI.inflate(-40, -40) 
        smallerRectAI = self.rectAI.inflate(-40, -40)
        if self.rectP1.colliderect(smallerRectHI):
            self.game.setPlayerLives(self.game.getPlayerLives() - 1)
            self.reset()
            print(str(self.game.getPlayerLives()))

        elif self.rectP1.colliderect(smallerRectAI):
            self.game.setMonsterLives(self.game.getMonsterLives() - 1)
            video = moviepy.editor.VideoFileClip(SPRITESHEET_PATH + 'me_MONSTERHURT_'+ str(random.randint(1,5)) +'.mp4', audio= False)
            video.preview()
            self.reset()
            print(str(self.game.getMonsterLives()))


        if self.game.getPlayerLives() == 0 :
            return (True, True, False)
        elif self.game.getMonsterLives() == 0:
            return (True, False, True)
        else:
            return (False, False, False)
    
    def move(self, rect, image):
        rect.move_ip(self.ItemVelocity[0], self.ItemVelocity[1])

        #if not (120 <= rect.left) or not (335 <= rect.top) or not (rect.right <= 390) or not (rect.bottom <= 505):
        if not (150 <= rect.centerx <= 390) or not (360 <= rect.centery <= 505):
            rect.center = self.oovPosition
            self.ItemThrown = False
    def reset(self):
        self.rectP1.center = self.P1InitialPosition
        self.rectHI.center = self.oovPosition
        self.rectAI.center = self.oovPosition
        self.ItemThrown = False
    def draw(self, displaySurface):
        displaySurface.blit(self.imageP1, self.rectP1)
        if self.ItemThrown:
            if self.isHarmful:
                displaySurface.blit(self.imageHI, self.rectHI)
            elif not self.isHarmful:            
                displaySurface.blit(self.imageAI, self.rectAI)

    def run(self,displaySurface):
        isEventOver = self.update()
        self.draw(displaySurface)
        return isEventOver
        
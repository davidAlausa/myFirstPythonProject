import pygame
from Config import *
from FUNCTIONALITY import Game
from monsterScreenATTACKBOARD import monsterScreenATTACKBOARD

class monsterScreenBACKGROUND():
    def __init__(self, Game):

        self.attckbrd = monsterScreenATTACKBOARD(Game)

        self.monsterEvent_BACKGROUND = pygame.image.load(SPRITESHEET_PATH + 'me_MAINSCREEN_BACKGROUND.png').convert()
        self.monsterEvent_ATTACKBOARD = pygame.image.load(SPRITESHEET_PATH + 'me_MAINSCREEN_ATTACKBOARD.png').convert_alpha()
        self.monsterEvent_MONSTERHEARTS_3 = pygame.image.load(SPRITESHEET_PATH + 'me_MAINSCREEN_MONSTERHEARTS_3.png').convert_alpha()
        self.monsterEvent_MONSTERHEARTS_2 = pygame.image.load(SPRITESHEET_PATH + 'me_MAINSCREEN_MONSTERHEARTS_2.png').convert_alpha()
        self.monsterEvent_MONSTERHEARTS_1 = pygame.image.load(SPRITESHEET_PATH + 'me_MAINSCREEN_MONSTERHEARTS_1.png').convert_alpha()
        self.monsterEvent_PLAYERHEARTS_3 = pygame.image.load(SPRITESHEET_PATH + 'me_MAINSCREEN_PLAYERHEARTS_3.png').convert_alpha()
        self.monsterEvent_PLAYERHEARTS_2 = pygame.image.load(SPRITESHEET_PATH + 'me_MAINSCREEN_PLAYERHEARTS_2.png').convert_alpha()
        self.monsterEvent_PLAYERHEARTS_1 = pygame.image.load(SPRITESHEET_PATH + 'me_MAINSCREEN_PLAYERHEARTS_1.png').convert_alpha()

        self.monsterEvent_BACKGROUND = pygame.transform.scale(self.monsterEvent_BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.monsterEvent_ATTACKBOARD = pygame.transform.scale(self.monsterEvent_ATTACKBOARD, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.monsterEvent_MONSTERHEARTS_3 = pygame.transform.scale(self.monsterEvent_MONSTERHEARTS_3, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.monsterEvent_MONSTERHEARTS_2 = pygame.transform.scale(self.monsterEvent_MONSTERHEARTS_2, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.monsterEvent_MONSTERHEARTS_1 = pygame.transform.scale(self.monsterEvent_MONSTERHEARTS_1, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.monsterEvent_PLAYERHEARTS_3 = pygame.transform.scale(self.monsterEvent_PLAYERHEARTS_3, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.monsterEvent_PLAYERHEARTS_2 = pygame.transform.scale(self.monsterEvent_PLAYERHEARTS_2, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.monsterEvent_PLAYERHEARTS_1 = pygame.transform.scale(self.monsterEvent_PLAYERHEARTS_1, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.monsterEvent_CURRENTMONSTERHEARTS = self.monsterEvent_MONSTERHEARTS_3
        self.monsterEvent_CURRENTPLAYERHEARTS = self.monsterEvent_PLAYERHEARTS_3

        self.game = Game

    def update (self):
        if self.game.getMonsterLives() == 3:
            self.monsterEvent_CURRENTMONSTERHEARTS = self.monsterEvent_MONSTERHEARTS_3
        elif self.game.getMonsterLives() == 2:
            self.monsterEvent_CURRENTMONSTERHEARTS = self.monsterEvent_MONSTERHEARTS_2
        elif self.game.getMonsterLives() == 1:
            self.monsterEvent_CURRENTMONSTERHEARTS = self.monsterEvent_MONSTERHEARTS_1
            
        if self.game.getPlayerLives() == 3:
            self.monsterEvent_CURRENTPLAYERHEARTS = self.monsterEvent_PLAYERHEARTS_3
        elif self.game.getPlayerLives() == 2:
            self.monsterEvent_CURRENTPLAYERHEARTS = self.monsterEvent_PLAYERHEARTS_2
        elif self.game.getPlayerLives() == 1:
            self.monsterEvent_CURRENTPLAYERHEARTS = self.monsterEvent_PLAYERHEARTS_1
            
    def draw(self,displaySurface):
        displaySurface.blit(self.monsterEvent_BACKGROUND, (0,0))
        displaySurface.blit(self.monsterEvent_ATTACKBOARD, (0,0))
        displaySurface.blit(self.monsterEvent_CURRENTMONSTERHEARTS, (0,0))
        displaySurface.blit(self.monsterEvent_CURRENTPLAYERHEARTS, (0,0))
        isEventOver = self.attckbrd.run(displaySurface)
        return isEventOver
    
    def run (self, displaySurface):
        self.update()
        isEventOver = self.draw(displaySurface)
        return isEventOver
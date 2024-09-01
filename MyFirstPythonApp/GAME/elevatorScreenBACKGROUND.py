import pygame
from Config import *
from FUNCTIONALITY import Game

class elevatorScreenBACKGROUND():
    def __init__(self,position,position2,position3,position4,position5):

        #initialising and resizing BACKGROUND 
        self.elevatorscreen_BACKGROUND_NOTSELECTED = pygame.image.load(SPRITESHEET_PATH + 'e_BACKGROUND.jpg').convert()
        self.elevatorscreen_BACKGROUND_NOTSELECTED = pygame.transform.scale(self.elevatorscreen_BACKGROUND_NOTSELECTED, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.elevatorscreen_BACKGROUND = self.elevatorscreen_BACKGROUND_NOTSELECTED

        self.elevatorscreen_BACKGROUND_G= pygame.image.load(SPRITESHEET_PATH + 'e_BACKGROUND_G.png').convert()
        self.elevatorscreen_BACKGROUND_G = pygame.transform.scale(self.elevatorscreen_BACKGROUND_G, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.elevatorscreen_BACKGROUND_2= pygame.image.load(SPRITESHEET_PATH + 'e_BACKGROUND_2.png').convert()
        self.elevatorscreen_BACKGROUND_2 = pygame.transform.scale(self.elevatorscreen_BACKGROUND_2, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.elevatorscreen_BACKGROUND_3= pygame.image.load(SPRITESHEET_PATH + 'e_BACKGROUND_3.png').convert()
        self.elevatorscreen_BACKGROUND_3 = pygame.transform.scale(self.elevatorscreen_BACKGROUND_3, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.elevatorscreen_BACKGROUND_4= pygame.image.load(SPRITESHEET_PATH + 'e_BACKGROUND_4.png').convert()
        self.elevatorscreen_BACKGROUND_4 = pygame.transform.scale(self.elevatorscreen_BACKGROUND_4, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.elevatorscreen_BACKGROUND_5= pygame.image.load(SPRITESHEET_PATH + 'e_BACKGROUND_5.png').convert()
        self.elevatorscreen_BACKGROUND_5 = pygame.transform.scale(self.elevatorscreen_BACKGROUND_5, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        #rects for mouse hovering
        self.floorbutton_1_rect = pygame.Rect(position[0], position[1], position[2], position[3])
        self.floorbutton_2_rect = pygame.Rect(position2[0], position2[1], position2[2], position2[3])
        self.floorbutton_3_rect = pygame.Rect(position3[0], position3[1], position3[2], position3[3])
        self.floorbutton_4_rect = pygame.Rect(position4[0], position4[1], position4[2], position4[3])
        self.floorbutton_5_rect = pygame.Rect(position5[0], position5[1], position5[2], position5[3])

    def update(self):
        if self.floorbutton_1_rect.collidepoint(pygame.mouse.get_pos()):
            self.elevatorscreen_BACKGROUND = self.elevatorscreen_BACKGROUND_G
            if pygame.mouse.get_pressed()[0]:
                return 1
            
        elif self.floorbutton_2_rect.collidepoint(pygame.mouse.get_pos()):
            self.elevatorscreen_BACKGROUND = self.elevatorscreen_BACKGROUND_2
            if pygame.mouse.get_pressed()[0]:
                return 2
        elif self.floorbutton_3_rect.collidepoint(pygame.mouse.get_pos()):
            self.elevatorscreen_BACKGROUND = self.elevatorscreen_BACKGROUND_3
            if pygame.mouse.get_pressed()[0]:
                return 3
        elif self.floorbutton_4_rect.collidepoint(pygame.mouse.get_pos()):
            self.elevatorscreen_BACKGROUND = self.elevatorscreen_BACKGROUND_4
            if pygame.mouse.get_pressed()[0]:
                return 4
        elif self.floorbutton_5_rect.collidepoint(pygame.mouse.get_pos()):
            self.elevatorscreen_BACKGROUND = self.elevatorscreen_BACKGROUND_5
            if pygame.mouse.get_pressed()[0]:
                return 5
        else:
            self.elevatorscreen_BACKGROUND = self.elevatorscreen_BACKGROUND_NOTSELECTED
            if pygame.mouse.get_pressed()[0]:
                return 0

    def draw(self, displaySurface):
        displaySurface.blit(self.elevatorscreen_BACKGROUND, (0,0))
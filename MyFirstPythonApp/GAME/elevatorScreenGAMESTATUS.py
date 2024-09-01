import pygame
from Config import *


class elevatorScreenGAMESTATUS():
    def __init__(self):
        # Initializing and resizing BACKGROUND 
        self.elevatorscreen_GAMESTATUS = pygame.image.load(SPRITESHEET_PATH + 'gs_TITLES.png').convert()
        self.elevatorscreen_GAMESTATUS = pygame.transform.scale(self.elevatorscreen_GAMESTATUS, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def draw(self, displaySurface, numOfKey, numOfLife, numOfFloorLvl):
        displaySurface.blit(self.elevatorscreen_GAMESTATUS, (0, 0))

        key_stat_path = SPRITESHEET_PATH + 'gs_KEYS_' + str(numOfKey) + '.png'
        life_stat_path = SPRITESHEET_PATH + 'gs_LIVES_' + str(numOfLife) + '.png'
        floor_level_stat_path = SPRITESHEET_PATH + 'gs_FLOORLEVEL_' + str(numOfFloorLvl) + '.png'

        elevatorscreen_KEYSTAT = pygame.image.load(key_stat_path).convert_alpha()
        elevatorscreen_KEYSTAT = pygame.transform.scale(elevatorscreen_KEYSTAT, (WINDOW_WIDTH, WINDOW_HEIGHT))
        displaySurface.blit(elevatorscreen_KEYSTAT, (0, 0))

        elevatorscreen_LIFESTAT = pygame.image.load(life_stat_path).convert_alpha()
        elevatorscreen_LIFESTAT = pygame.transform.scale(elevatorscreen_LIFESTAT, (WINDOW_WIDTH, WINDOW_HEIGHT))
        displaySurface.blit(elevatorscreen_LIFESTAT, (0, 0))

        elevatorscreen_FLOORLEVELSTAT = pygame.image.load(floor_level_stat_path).convert_alpha()
        elevatorscreen_FLOORLEVELSTAT = pygame.transform.scale(elevatorscreen_FLOORLEVELSTAT, (WINDOW_WIDTH, WINDOW_HEIGHT))
        displaySurface.blit(elevatorscreen_FLOORLEVELSTAT, (0, 0))
                    
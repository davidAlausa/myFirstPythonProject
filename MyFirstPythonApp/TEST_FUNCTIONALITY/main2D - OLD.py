import pygame
from pygame.locals import *
import sys
from classes import game
import random

class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
 
    def on_init(self):
        FPS = 60
        FramePerSec = pygame.time.Clock()

        BLUE  = (0, 0, 255)
        RED   = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(WHITE)
        pygame.display.set_caption("Game")
        self._running = True

 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):

        is_playing = True
        print('WELCOME TO ESCAPE ROOM LITE by David Alausa\n\n\n')

        while is_playing == True:
            case = input('\n\nEnter 1 to play or 2 to exit:\t')
            try:
                case = int(case)
            
                while case != 1 and case !=2:
            
                    print('\n\tThis is not a valid option.... try again')
                    case = int(input('\n\nEnter 1 to play or 2 to exit:\t'))
        
                if case == 1:
                    break
                elif case == 2:
                    print('leaving now.....\n\n')
                    self.on_cleanup
                    sys.exit()
                    
            except ValueError:
                print("\n\n---*Invalid input. Please enter a valid integer*---")


    def on_render(self):
        
        current_game = game.Game()
        gameStatus = False

        #Game loop begins
        while gameStatus == False:
            current_game.baseMenu()
            gameStatus = current_game.getGameStatus()
            pygame.display.update()

        if current_game.checkEndGameStatus():
            print('\n\n\tYAYYYY. You won with '+ str(current_game.player.getLives()) +' lives remaining!!!')
            pygame.display.update()

        else:
            print('\n\n\tOH NO! Yikes.... looks like the monster got you.')
            pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute

class Monster(pygame.sprite.Sprite):
    
    def __init__(self):
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 400

        super().__init__() 
        self.image = pygame.image.load("images\monster.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,self.SCREEN_WIDTH-40),0) 
 
    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):

    def __init__(self):

        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 400

        super().__init__() 
        self.image = pygame.image.load("imaes/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < self.SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 
         
P1 = Player()
E1 = Monster()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()
     
    .fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)

import sys
from .classes import game

def newGame():
    current_game = game.Game()
    gameStatus = False

    while gameStatus == False:
        current_game.baseMenu()
        gameStatus = current_game.getGameStatus()
        

def willPlay(case):
            if case == 1:
                newGame()
            elif case == 2:
                print('leaving now.....\n\n')
                exit()

def programStart():
    is_playing = True
    print('WELCOME TO ESCAPE ROOM LITE by David Alausa\n\n\n')

    while is_playing == True:
        case = input('\n\nEnter 1 to play or 2 to exit:\t')
        try:
            case = int(case)
        
            while case != 1 and case !=2:
        
                print('\n\tThis is not a valid option.... try again')
                case = int(input('\n\nEnter 1 to play or 2 to exit:\t'))
    
            willPlay(case)
            exit()
        except ValueError:
            print("\n\n---*Invalid input. Please enter a valid integer*---")
         
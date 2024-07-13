
import sys

is_playing = True
print('WELCOME TO ESCAPE ROOM LITE by David Alausa\n\n\n')

while is_playing == True:
    case = input('\n\nEnter 1 to play or 2 to exit:\t')
    try:
        case = int(case)
    
        while case != 1 and case !=2:
    
            print('\n\tThis is not a valid option.... try again')
            case = int(input('\n\nEnter 1 to play or 2 to exit:\t'))
    
        def willPlay(case):
            if case == 1:
                print('looooool')
            elif case == 2:
                print('leaving now.....')
                sys.exit()
        
        willPlay(case)
    
    except ValueError:
         print("\n\n---*Invalid input. Please enter a valid integer*---")
         

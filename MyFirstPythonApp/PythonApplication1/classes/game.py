import random
import time
from .hotel import Hotel
from .monster import Monster
from .player import Player

class Game:
    def __init__(this):
        this.hotel = Hotel()
        this.monster = Monster()
        this.player = Player()
        this.isOver = False
        this.key = random.randint(2,5)
        if this.key == this.monster.floorLevel:
            while this.key == this.monster.floorLevel:
                this.key = random.randint(2,5)

        this.keyInventoryCount = 0

        this.CRED = '\033[91m'      #RED
        this.CEND = '\033[0m'    #NORMAL
        this.CGREEN  = '\33[32m' #GREEN
        this.CBLUE   = '\33[34m'    #BLUE
        this.CVIOLET = '\33[35m'    #VIOLET
    def getGameStatus(this):
        return this.isOver
    
    def setGameStatus(this, newValue):
        this.isOver = newValue
    
    def validateElevatorFloor(this, proposedFloor):

        currentFloor = this.hotel.getFloor() 

        if proposedFloor == currentFloor:
                print('\n\n\tElevator: ' +this.CGREEN + '"You are on this floor silly! bzzzrrttt!. Pick. a. floor."\t' + this.CEND)
                return False

        if proposedFloor > 5 or proposedFloor < 0:
                print('\n\n\tElevator: ' +this.CGREEN + '"We cannot afford that level of floors! bzzzrrttt!. Pick. a. floor. Between 1-5 BZZRRTT."\t' + this.CEND)
                return False

        return True

    def baseMenu(this):

        CGREEN  = '\33[32m' #GREEN
        functionFailure = True

        while functionFailure == True:
            print('\n\n\tYou are on FLOOR ' + str(this.hotel.getFloor()))
            elevatorChoice = input('\n\n\tElevator: ' +this.CGREEN + '"Pick. a. floor. bzzrttt"\t' + this.CEND)

            try:
                elevatorChoice = int(elevatorChoice)

                while not this.validateElevatorFloor(elevatorChoice):
                    elevatorChoice = int(input('\n\t'))

                functionFailure == False

                this.checkElevatorChoice(elevatorChoice)

                this.monster.moveMonster()

                while this.hotel.getFloor == this.monster.floorLevel:
                    this.monster.moveMonster()

            except ValueError:
                print("\n\n---*Invalid input. Please enter a valid integer*---")


    def keyFound(this):
        this.keyInventoryCount +=1 
        print('\n\n\tYou found a Key! You now have ' + str(this.keyInventoryCount) + ' keys in your possession.')

        if this.keyInventoryCount != 3:

            print ('Good Luck!')

            this.key = random.randint(2,5)
            if this.key == this.monster.floorLevel:
                while this.key == this.monster.floorLevel:
                    this.key = random.randint(2,5)

        elif this.keyInventoryCount == 3:

            print ('This means that you can escape!!! Head back to floor one NOW!!!')

    def monsterEvent(this):
        

        print(this.CRED + '\n\n\tMONSTER: muhhaahhahahHAHAHAHHAHAH' + this.CEND)
        print("\n\n\tIt's the " + this.CRED + "MONSTER" + this.CEND +"!\n\n\t\t Enter '1' to ATTACK or Enter '2' to Defend")
        print('\n\n THE FIGHT STARTS IN 3...')
        time.sleep(2)
        print('\n2...')
        time.sleep(2)
        print('\n1... \n\n----------------------------------------------------------------------------\n')

        # Insert Monster Fighting Functionality
        while this.monster.getLives() > 0 and this.player.getLives() > 0:
            action = random.randint(1, 3)
            RandomActionButton = random.randint(0,9)
            print("\n\nThe " + this.CRED + "MONSTER " + this.CEND + ".....")
            time.sleep(2)

            if action == 1:
                start_time = time.time()
                defend = input(this.CRED + "ATTACKS! Enter '"+str(RandomActionButton)+"' to Defend:\t" + this.CEND)

                if time.time() - start_time <= 2 and defend == str(RandomActionButton):
                    print(this.CBLUE + "You defended successfully!" + this.CEND)
                else:
                    print(this.CRED + "You failed to defend!" + this.CEND)
                    this.player.setLives(this.player.lives - 1)

            elif action == 2:
                print(this.CBLUE + "DEFENDS!" + this.CEND)

            elif action == 3:
                start_time = time.time()
                print(this.CVIOLET + "TAUNTS!" + this.CEND)

                attack = input("Enter "+str(RandomActionButton)+"' to Attack:\t")
                if time.time() - start_time <= 2 and attack == str(RandomActionButton):
                    print(this.CGREEN + "You attacked successfully!" + this.CEND)
                    this.monster.setLives(this.monster.lives - 1)
                else:
                    print(this.CRED + "MONSTER: TOO SLOW (almost got me there....)" + this.CEND)

        if this.player.getLives() == 0:
            print(this.CRED + "\n\nMONSTER: HAHAHAHHAHAH. YOUR WEAKER THAN I THOUGHT" + this.CEND)
            this.isOver = True

        elif this.monster.getLives() == 0:
            print(this.CRED + "\n\nMONSTER: Ouch... That kinda hurt..." + this.CEND)
            print("\nYou beat the monster with " + str(this.player.getLives()) + " left. Be careful!!!")




    def emptyFloor(this):
        print('still wip')

    def checkElevatorChoice(this, choice):
        print('\n\n\tGoing to floor ' + str(choice )+ '. Opening door in:')
        print('\n\t3...')
        time.sleep(2)
        print('\n\t2....')
        time.sleep(2)
        print('\n\t1...')   

        this.hotel.setFloor(choice)

        if choice == this.monster.floorLevel:
            this.monsterEvent()
        
        elif choice == this.key:
            this.keyFound()
        
        else:
            this.emptyFloor()

        
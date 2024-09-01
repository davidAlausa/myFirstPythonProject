import random
import time
import string
from Hotel import Hotel
from Monster import Monster
from Player import Player

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

        this.keyInventoryCount = 1

        this.CRED = '\033[91m'      #RED
        this.CEND = '\033[0m'    #NORMAL
        this.CGREEN  = '\33[32m' #GREEN
        this.CBLUE   = '\33[34m'    #BLUE
        this.CVIOLET = '\33[35m'    #VIOLET
        this.CBLINK    = '\33[5m' #BLINK

    def getGameStatus(this):
        return this.isOver
    
    def checkEndGameStatus(this):
        if this.player.getLives() > 0 and this.keyInventoryCount == 3 and this.hotel.getFloor() == 1:
            return True
        else:
            return False
        
    def setGameStatus(this, newValue):
        this.isOver = newValue
    
    def validateElevatorFloor(this, proposedFloor):

        currentFloor = this.hotel.getFloor() 

        if proposedFloor == currentFloor:
            print('\n\n\tElevator: ' +this.CGREEN + '"You are on this floor silly! bzzzrrttt!. Pick. a. floor:"\t' + this.CEND)
            return False
        #######
        elif proposedFloor == 0 or proposedFloor == None:
            return False

        else:
            return True

    def baseMenu(this):
        if this.keyInventoryCount == 3 and this.hotel.getFloor() == 1:
            this.isOver = True
            return

        CGREEN  = '\33[32m' #GREEN

        print('\n\n\tYou are on FLOOR ' + str(this.hotel.getFloor()))
        elevatorChoice = input('\n\n\tElevator: ' +this.CGREEN + '"Pick. a. floor. bzzrttt:"\t' + this.CEND)
        try:
            elevatorChoice = int(elevatorChoice)

            while not this.validateElevatorFloor(elevatorChoice):
                elevatorChoice = int(input('\n\t'))
            
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

            print ('\tGood Luck!')

            this.monster.moveMonster()
            this.key = random.randint(2,5)
            if this.key == this.monster.floorLevel:
                while this.key == this.monster.floorLevel:
                    this.key = random.randint(2,5)

        elif this.keyInventoryCount == 3:

            print ('\tThis means that you can escape!!! Head back to floor one NOW!!!')

    def monsterEvent(this):
        
        this.monster.resetLives()

        print(this.CRED + '\n\n\tMONSTER: muhhaahhahahHAHAHAHHAHAH' + this.CEND)
        print("\n\n\tIt's the " + this.CRED + "MONSTER" + this.CEND +"!\n\n\t\t Enter the correct key to win!!")
        print('\n\n THE FIGHT STARTS IN 3...')
        time.sleep(1)
        print('\n2...')
        time.sleep(1)
        print('\n1...')
        time.sleep(1)
        print('\n\n----------------------------------------------------------------------------\n')
        # Insert Monster Fighting Functionality
        while this.monster.getLives() > 0 and this.player.getLives() > 0:
            action = random.randint(1, 3)
            RandomActionButton = random.choice(string.ascii_letters + string.digits + string.punctuation)
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

                attack = input("Enter '"+str(RandomActionButton)+"' to Attack:\t")
                if time.time() - start_time <= 2 and attack == str(RandomActionButton):
                    print(this.CGREEN + "You attacked successfully!" + this.CEND)
                    this.monster.setLives(this.monster.lives - 1)
                else:
                    this.monster.monstertaunts()

        if this.player.getLives() == 0:
            print(this.CRED + "\n\nMONSTER: HAHAHAHHAHAH. YOUR WEAKER THAN I THOUGHT" + this.CEND)
            this.setGameStatus(True)

        elif this.monster.getLives() == 0:
            print(this.CRED + "\n\nMONSTER: Ouch... That kinda hurt..." + this.CEND)
            print("\nYou beat the monster with " + str(this.player.getLives()) + " lives left. Be careful!!!")

            this.monster.moveMonster()
            if this.monster.floorLevel == this.key:
                while this.monster.floorLevel == this.key:
                    this.monster.moveMonster()





    def emptyFloor(this):
        event = random.randint(1,5)
        
        if event == 1:
            print('\n\n\t"The lift doors slide open to reveal... nothing! Well, except for a lonely dust bunny contemplating its existence."')
            time.sleep(2)
        elif event == 2:
            print('\n\n\t"The lift opens to an empty floor. You hear the distant echo of your own disappointment."')
            time.sleep(2)
        elif event == 3:
            print('\n\n\t"You step out to... an empty floor. Perhaps the universe is telling you to try again."')
            time.sleep(2)
        elif event == 4:
            print('\n\n\t"As the door opens you find a '+this.CGREEN+'1UP MARIO MUSHROOM '+this.CEND+'on the floor"')
            time.sleep(2)
            print('\n\n\t"You question the creator\'s lack of originality as you ingest the mushroom"')
            time.sleep(2)
            if not this.player.getLives() > 2:
                this.player.setLives(this.player.getLives() + 1)
                print(this.CGREEN + '\n\nYOU GAINED 1 LIFE. ' + str(this.player.getLives()) + ' lives remaining' + this.CEND)
                time.sleep(1.5)
                print('\n\n\t"tastes green...."')
            else:
                print('\n\n\t"You instantly feel sick... Maybe you should lay off the mushrooms for a while..."')
            time.sleep(1)

        elif event == 5:
            print(this.CRED + "\n\n\tMONSTER: ehheeheheh...... "+ this.CBLINK +" I CAN SMELL YOU....."+ this.CEND)
            print('\n\n\t')
            time.sleep(2)

    def checkElevatorChoice(this, choice):
        print('\n\n\tGoing to floor ' + str(choice )+ '. Opening door in:')
        print('\n\t\t3...')
        time.sleep(1.5)
        print('\n\t\t2....')
        time.sleep(1.5)
        print('\n\t\t1...')   
        time.sleep(1.5)
        this.hotel.setFloor(choice)

        if choice == this.monster.floorLevel:
            this.monsterEvent()
        
        elif choice == this.key:
            this.keyFound()
        
        else:
            this.emptyFloor()

    def getKeyInventoryCount(this):
        return this.keyInventoryCount
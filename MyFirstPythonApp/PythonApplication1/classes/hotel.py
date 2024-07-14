import random
import time
import monster

class Hotel:
    def __init__(this):
        this.floor = 1
        this.monster = random.randint(2,5)
        this.key = random.randint(2,5)
        this.keyInventoryCount = 0

    def keyFound(this):
        print('\n\n\tYou found a Key! You now have ' + thiskeyInventoryCount + ' keys in your possession.')

        if this.keyInventoryCount != 3:

            print ('Good Luck!')
            thiskeyInventoryCount += 1
        
        elif thiskeyInventoryCount == 3:

            print ('This means that you can escape!!! Head back to floor one NOW!!!')

    def monsterEvent():
        CRED = '\033[91m'
        CEND = '\033[0m'
        print(CRED + '\n\n\tmuhhaahhahahHAHAHAHHAHAH' + CEND)
        print("\n\n\tIt's the " + CRED + "MONSTER" + CEND +"\n\n\t\t! Enter 'A' to ATTACK or Enter 'D' to Defend")
        print('\n\n THE ATTACK')
        time.sleep(2)
        print('\n\BEGINS')
        time.sleep(2)
        print('\n\tNOW\n\n----------------------------------------------------------------------------\n')

        newMonster = Monster()
    def emptyFloor():
        print('still wip')

    def checkElevatorChoice(this, choice):
        print('\n\n\tGoing to floor' + choice + '. Opening door in:')
        time.sleep(2)
        print('\n\t3...')
        time.sleep(2)
        print('\n\t2....')
        time.sleep(2)
        print('\n\t1...')   

        this.floor = choice

        if choice == this.monster:
            this.monsterEvent()
        
        elif choice == this.key:
            this.keyFound()
        
        else:
            this.emptyFloor()

        
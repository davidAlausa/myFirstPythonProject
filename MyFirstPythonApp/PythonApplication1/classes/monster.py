import random
import time

class Monster:
    def __init__(this):
        this.floorLevel = random.randint(2,5)
        this.lives = 3
        this.CRED = '\033[91m'      #RED
        this.CEND = '\033[0m'    #NORMAL
        this.CGREEN  = '\33[32m' #GREEN
        this.CVIOLET2 = '\33[95m' # VIOLET
    def moveMonster(this):
        this.floorLevel = random.randint(2,5)

    def getLives(this):
        return this.lives

    def setLives(this, newValue):
        this.lives = newValue
    
    def resetLives(this):
        this.lives = 3
    
    def monstertaunts(this):
        taunt = random.randint(1,10)

        if taunt == 1:
            print(this.CRED + "MONSTER: PFFFFFFT. WHAT WAS THAT??!!!" + this.CEND)
        elif taunt == 2:
            print(this.CRED + "MONSTER: MY GRANDMA CAN HIT HARDER THAN THAT God rest her soul...." + this.CEND)
        elif taunt == 3:
            print(this.CRED + "MONSTER: YAWWWWWNNN. OH! ITS MY TURN NOW." + this.CEND)
        elif taunt == 4:
            print(this.CRED + "MONSTER: WOW THAT WAS WEAK..... DO YOU NEED A TIME OUT OR SOMETHING?" + this.CEND)
            time.sleep(1)
            print(this.CRED + "\nMONSTER: SIKE!!!" + this.CEND)
            time.sleep(0.5)
        elif taunt == 5:
            print(this.CRED + "MONSTER: WEEAVEE!!" + this.CEND)
        elif taunt == 6:
            print(this.CGREEN + "MONSTER: AHAHAHHAHA THAT TICKLES. MY TURN" + this.CEND)
            time.sleep(1)
            print(this.CRED + "\nMONSTER: MY TURN." + this.CEND)
        elif taunt == 7:
            print(this.CRED + "MONSTER: CHILE- ANYWAYS..." + this.CEND)
        elif taunt == 8:
            print(this.CRED + "MONSTER: ... are you serious right now?" + this.CEND)
        elif taunt == 9:
            print(this.CRED + "MONSTER: AHHHHH IT HURTS...... HOW PATHETIC THAT WAS" + this.CEND)
        elif taunt == 10:
            print(this.CRED + "MONSTER:" + this.CEND + this.CVIOLET2 + " *Drake Voice* EMBARASSING" + this.CEND)
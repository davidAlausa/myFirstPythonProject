import random
import time

class Monster:
    def __init__(this):
        this.floorLevel = random.randint(2,5)
        this.lives = 3

    def moveMonster(this):
        this.floorLevel = random.randint(2,5)

    def getLives(this):
        return this.lives

    def setLives(this, newValue):
        this.lives = newValue

        
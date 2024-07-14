class Player:
    def __init__(this):
        this.lives = 3

    def checkLives(this):
        if this.lives <= 0:
            return True
        elif this.lives > 3:
            return False

    def getLives(this):
        return this.lives
    
    def setLives(this, change):
        this.lives = change
        this.checkLives()

        
import random

class Game(object):
    firstCount = 0
    secondCount = 0

    playerNumber = 0

    def play(self):
        currentCount = random.choice(range(1,7))
        if (self.playerNumber == 0):
            self.firstCount += currentCount
            self.playerNumber = 1
            if self.firstCount == self.secondCount:
                return 1
            if self.firstCount >= 30:
                return 2
        else:
            self.secondCount += currentCount
            self.playerNumber = 0
            if self.secondCount == self.firstCount:
                return 3
            if self.secondCount >= 30:
                return 4
        return 0

def playGame():
    game = Game()
    while(True):
        res = game.play()
        if res == 2 or res == 4:
            return 1
        elif res == 1 or res == 3:
            return 0

s = 0
for i in range(1000):
    s += playGame()

print s/1000.0

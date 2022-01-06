from random import randint


class Game:
    def __init__(self, rand=0, loser=0):
        self.rand = randint(1, 3)

    def reset(self):
        self.rand = randint(1, 3)

    def guess(self, num):
        return self.rand == num

    #  randomly picks a door until it finds a losing door that wasn't the user's guess
    def setLoser(self, guess):
        loser = randint(1, 3)
        while loser == guess or loser == self.rand:
            loser = randint(1, 3)
        print(f"Removed: {loser}")
        self.loser = loser

    def switch(self, guess):
        newGuess = randint(1, 3)
        while newGuess == guess or newGuess == self.loser:
            newGuess = randint(1, 3)
        print(f"New Guess: {newGuess}")
        return newGuess

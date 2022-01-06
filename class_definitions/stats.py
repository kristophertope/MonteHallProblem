class Stats:
    def __init__(self, wins=0, losses=0):
        self.wins = wins
        self.losses = losses

    def won(self):
        self.wins += 1

    def lost(self):
        self.losses += 1

    def reset(self):
        self.wins = 0
        self.losses = 0

    def winPercent(self):
        if self.wins == 0:
            return '0%'
        return "{:.0%}".format(self.wins / (self.wins + self.losses))

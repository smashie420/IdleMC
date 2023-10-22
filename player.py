class Player:
    def __init__(self):
        self.minecoins = 0
        
        self.miningSpeed = 1
        self.miningDelay = 1

        self.upgrades = []

    def giveMineCoins(self,amount):
        if amount <= 0: return
        self.minecoins += amount
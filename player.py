class Player():
    def __init__(self):
        self.minecoins = 0
        
        self.miningSpeed = 1
        self.miningDelay = 1

        self.upgrades = []
        self.lastLogin = ''



    def getMineCoins(self):
        return self.minecoins
    def setMineCoins(self,amount):
        if type(amount) != int:
            raise ValueError
        self.minecoins += amount
        
        
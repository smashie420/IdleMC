class Player():
    def __init__(self):
        self.minecoins = 0
        
        self.miningSpeed = 1
        self.miningDelay = 2

        self.upgrades = []
        self.inventory = []


        self.lastLogin = '0'



    def getMineCoins(self):
        return self.minecoins
    def setMineCoins(self,amount):
        if type(amount) != int:
            raise ValueError
        self.minecoins += amount
        
        
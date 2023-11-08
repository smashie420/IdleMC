from items import Items

class Player:
    def __init__(self):
        self.minecoins = 0
        self.miningSpeed = 1
        self.miningDelay = 2


        self.upgrades = []
        self.inventory = []

        self.lastLogin = '0'

        #for i in range(0, len(Items().blocks)): # Populate the list with all the blocks
        #    self.inventory.append({'name': Items().blocks[i]['name'], 'quantity':0})



    def getMineCoins(self):
        return self.minecoins
    def setMineCoins(self,amount):
        if type(amount) != int:
            raise ValueError
        self.minecoins += amount
    def appendInventory(self, item):
        #item = 
        #self.inventory.append(item)

        # THERE IS TWO ARRAYS BECAUSE OF THE SAVE FILE
        print("HI")
        
        
from items import Items

class Player:
    def __init__(self):
        self.minecoins = 0
        self.miningSpeed = 1
        self.miningDelay = 0.1


        self.upgrades = []
        self.inventory = []

        self.lastLogin = '0'



    def getMineCoins(self):
        return self.minecoins
    def setMineCoins(self,amount):
        if type(amount) != int:
            raise ValueError
        self.minecoins += amount
    def appendInventory(self, item):
        '''
            Appends an array of items (blocks) into the players inventory

        Args:
            item (array): 
            
        Returns:
            void: returns nothing    
        '''
        for i in range(0,len(self.inventory)):
            if item[i]['name'] == self.inventory[i]['name']: # IF
                self.inventory[i]['quantity'] += item[i]['quantity']

        #print(f'player.py:\n        AFTER appendInventory(item): {item}')
        #print(f'player.py:\n        AFTER Self Inventory: {self.inventory}')

    def print_inventory(self):
        for block in self.inventory:
            print(f"{block['name']} x{block['quantity']}")

        
        
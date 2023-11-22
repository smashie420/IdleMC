from items import Items
from extras.colors import bcolors

class Player:
    def __init__(self):
        self.minecoins = 0

        self.miningLvl = 1
        self.miningDelay = 1
        self.miningSpeed = self.miningDelay / self.miningLvl

        self.upgrades = []
        self.inventory = []

        self.lastLogin = '0'

    def getMineCoins(self):
        return self.minecoins
    def setMineCoins(self,amount):
        if type(amount) != int:
            raise ValueError
        self.minecoins = amount
    def addMineCoins(self, amount):
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
            if item[i]['name'] == self.inventory[i]['name']:
                self.inventory[i]['quantity'] += item[i]['quantity']

        #print(f'player.py:\n        AFTER appendInventory(item): {item}')
        #print(f'player.py:\n        AFTER Self Inventory: {self.inventory}')

    def getInventory(self):
        return self.inventory
    
    def removeBlockFromInventory(self, block_name, quantity=1):
        '''
            Appends an array of items (blocks) into the players inventory

        Args:
            block_name (str): the blocks name 
            quantity (int): the amount to remove
            
        Returns:
            void: returns nothing
        '''
        for i in range(0,len(self.inventory)):
            if self.inventory[i]['name'] == block_name:
                    self.inventory[i]['quantity'] -= quantity
                
    #def getInventory(self):
    #    return self.inventory
    
    def getOnhandBlock(self, block_name):
        ''' 
        Gets the quantity of the block from a players inventory
        '''
        for block in self.inventory: # Searches the array for the block we're looking for
            if block['name'] == block_name:
                return block['quantity']

    def print_inventory(self):
        print(f"{bcolors.OKCYAN}Inventory{bcolors.ENDC}")
        for block in self.inventory:
            print(f" {block['name']} x{block['quantity']}")

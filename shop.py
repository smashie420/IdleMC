from items import Items
from extras.colors import bcolors

class Shop:
    def __init__(self, player):
        '''
        Args:
            player(class): Give the player class
        '''
        self.player = player

    def sellResource(self, resource, quantity):
        item = Items()
        player = self.player
        resourceCost = item.getWorth(resource)

        # Remove Resource From Inventory
        player.removeBlockFromInventory(resource, quantity)

        # Add Money
        player.addMineCoins(resourceCost * quantity)

        print(f"{bcolors.OKGREEN}Sold {resource} for ${resourceCost * quantity}!{bcolors.ENDC}")

    def calculateWorth(self, block_name, quantity):
        return Items().getWorth(block_name) * quantity
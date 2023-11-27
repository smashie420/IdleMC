from items import Items
from extras.colors import bcolors
import time

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
    
    def buyTool(self, tool_name):
        player_mineCoins = self.player.minecoins
        player_upgrades = self.player.upgrades
        tool_cost = Items().getItemWorth(tool_name)

        if self.player.checkIfHasUpgrade(tool_name):
            print(f"{bcolors.WARNING}You already have a {tool_name}!{bcolors.ENDC}")
            time.sleep(2.5)
            return
        if player_mineCoins < tool_cost: # Check if player has enough money for the tool
            print(f"{bcolors.WARNING}You don't have enough funds for {tool_name}!{bcolors.ENDC}")
            time.sleep(2.5)
            return

        # Remove money from player
        self.player.subtractMineCoins(tool_cost)

        # Add item to players upgrade
        player_upgrades.append(Items().getItem(tool_name))

        print(self.player.upgrades)
        time.sleep(3)
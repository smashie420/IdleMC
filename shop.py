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
        """Sells resource

        Args:
            resource (str): Resources string name
            quantity (int): The quantity to sell

        """    
        item = Items()
        player = self.player
        resourceCost = item.getWorth(resource)

        # Remove Resource From Inventory
        player.removeBlockFromInventory(resource, quantity)

        # Add Money
        player.addMineCoins(resourceCost * quantity)

        print(f"{bcolors.OKGREEN}Sold {resource} for ${resourceCost * quantity}!{bcolors.ENDC}")

    def calculateWorth(self, block_name, quantity):
        """Calculates the worth of blocks

        Args:
            block_name (str): The block name
            quantity (int): Quantity to sell

        Returns:
            int: The mathematical result of multiplying the price of the block * quantity
        """    
        return Items().getWorth(block_name) * quantity
    
    def buyTool(self, tool_name):
        """Buys a tool

        Args:
            a (int): _description_
            b (str): _description_
            c (bool, optional): _description_. Defaults to True.

        Returns:
            bool: _description_
        """    
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

        print(f"{bcolors.OKGREEN}Bought {tool_name} for ${tool_cost}{bcolors.ENDC}\n{bcolors.BOLD}Remaing minecoins ${player_mineCoins}{bcolors.ENDC}")
        time.sleep(3)       
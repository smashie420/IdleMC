from items import Items
from player import Player

class Shop:
    def sellResource(resource):
        item = Items()
        player = Player()
        resourceCost = item.getWorth(resource)

        # Remove Resource From Inventory
        player.removeBlockFromInventory(resource)

        # Add Money
        player.addMineCoins(resourceCost)

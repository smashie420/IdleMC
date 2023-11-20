#!/usr/bin/env python3

# PIP INSTALL REQUIREMENTS:
#   keyboard
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#from player import Player

#from items import Items
#items = Items()
#print(items.getWorth("Diamond"))
from game import IdleMC
game = IdleMC() 


game.loadData() # This changes the class from a class 'player.Player' class to a class 'dict'
#game.gatherMaterials()
#print("\n\nINVENTORY: ")
#game.player.print_inventory()

print(f"BEFORE SELL {game.player.getMineCoins()}")
game.player.print_inventory()
game.sellResource('Cobblestone')

print(f"AFTER SELL {game.player.getMineCoins()}")
game.player.print_inventory()

game.saveData()
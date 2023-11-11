#!/usr/bin/env python3

# PIP INSTALL REQUIREMENTS:
#   keyboard
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#from player import Player
from game import IdleMC

#from items import Items
#items = Items()
#print(items.getWeights())

game = IdleMC() 


game.loadData() # This changes the class from a class 'player.Player' class to a class 'dict'
game.gatherMaterials()

print("\n\n INVENTORY: ")
game.player.print_inventory()
game.saveData()
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

game = IdleMC() 

game.loadData()
print(game.player['minecoins'])
game.gatherMaterials()
#user.setMineCoins(1000)
game.saveData()

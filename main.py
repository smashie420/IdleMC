#!/usr/bin/env python3

# PIP INSTALL REQUIREMENTS:
#   keyboard
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

from game import IdleMC
from items import Items
from extras.colors import bcolors
import keyboard
import time
import os
from menu import menu

game = IdleMC() 
game.loadData() # This changes the class from a class 'player.Player' class to a class 'dict'
game.initilizeShop() # Once data loads, update the shop to have the current player data

UI = menu(game)

if __name__ == '__main__':
    while(True):
        os.system('cls')
        UI.print_game_logo()
        UI.print_options()
        event = keyboard.read_event(suppress=True)
        if (event.event_type == keyboard.KEY_DOWN) and event.name == 'w':
            UI.goMining()
        if (event.event_type == keyboard.KEY_DOWN) and event.name == 'e':
            UI.sellResources()
        if (event.event_type == keyboard.KEY_DOWN) and event.name == 't':
            UI.shop()
        if (event.event_type == keyboard.KEY_DOWN) and event.name == 'r':
            UI.inventory()
        if (event.event_type == keyboard.KEY_DOWN) and event.name == 'a':
            UI.stats()
        if (event.event_type == keyboard.KEY_DOWN) and event.name == 'q':
            print("Quitting.")
            break

game.saveData()
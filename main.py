#!/usr/bin/env python3

# PIP INSTALL REQUIREMENTS:
#   keyboard
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
from player import Player
from game import IdleMC

game = IdleMC() 
user = Player()

game.gatherMaterials(user)

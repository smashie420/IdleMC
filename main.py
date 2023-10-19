#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
from player import Player

user = Player()
user.loadData()

user.gatherMaterials()
print(user.minecoins)
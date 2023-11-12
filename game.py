# Used to serialize and decode json and used to detect if savefile exists
import json
import os

# Used for sleeping (gatherMaterials)
import time
# Used for random rolls (gatherMaterials)
from random import randint, choices
# Used to detect if a key is pressed (gatherMaterials)
import keyboard
# Used for mining
import threading

# Imports from files i've created:
from player import Player
from items import Items
from exceptions import FileNotExistant
from extras.colors import bcolors

# File name for creating/writing/saving data
saveFilename = 'data.json'


# !!! Possible Feature Addition encrypt the data.json with md5 or some other hashing method 
# !!! to prevent players from editing their save
class IdleMC:
    def __init__(self):
        self.player = Player()

    def gatherMaterials(self):
        miner = threadedGoMining(self.player)
        thread = threading.Thread(target=miner.start, args=())

        print(f"{bcolors.WARNING}!!! AT ANYTIME PRESS 'q' to stop mining !!!{bcolors.ENDC}")
        time.sleep(2)
        os.system('cls')
        thread.start()

        while True:
            if keyboard.is_pressed('q'):
                miner.stop()
                break

    def blankInventory():
        '''
        Will get every block inside of items.py and format them AKA a blank inventory

        Returns:
            [{'name': 'Dirt', 'quantity': 0}, {'name': 'Cobblestone', 'quantity': 0}, ... {'name': 'Diamond', 'quantity': 0}]
        
        '''
        result = []
        for i in range(0, len(Items().blocks)):
            result.append({'name': Items().blocks[i]['name'], 'quantity':0})
        return result


    # FIX THIS IT SHOULD SAVE ERVERYTHING NOT JUST VARAIBLES IN GAME.PY !!!
    def saveData(self):
        if not os.path.exists(saveFilename):
            open(saveFilename, 'a').close()

        self.lastLogin = time.time()
        saveFile = open(saveFilename,'w', encoding="utf-8") 
        saveFile.write(json.dumps(self, default=vars))

    def loadData(self):
        if not os.path.exists(saveFilename): # If file doesnt exist then create new one
            saveFile = open(saveFilename,'w', encoding="utf-8") 


            #for i in range(0, len(Items().blocks)): # Populate the list with all the blocks, needed for making sure the indexes matches with the platers inventory
            #    self.player.inventory.append({'name': Items().blocks[i]['name'], 'quantity':0})
            self.player.inventory = IdleMC.blankInventory()

            saveFile.write(json.dumps(self, default=vars))


            #raise FileNotExistant
        
        saveFile = open(saveFilename,'r') 

        saveFileDecoded = json.load(saveFile)

        loadedPlayer = Player()
        for key, value in saveFileDecoded['player'].items():
            setattr(loadedPlayer,key,value)
            


        self.player = loadedPlayer

'''
This class is used in "IdleMC" class for method gatherMaterials()
'''
class threadedGoMining:
    def __init__(self, player):
        self._stop = threading.Event()
        self.player = player
        self.items = Items()
        self.resourcesGathered = []

    def start(self):

        self.resourcesGathered = IdleMC.blankInventory() # Returns a blank slate of blocks

        #for i in range(0, len(self.items.blocks)): # Populate the list with all the blocks, needed for making sure the indexes matches with the platers inventory
        #    self.resourcesGathered.append({'name': self.items.blocks[i]['name'], 'quantity':0})
        #print(self.resourcesGathered)

        while not self._stop.is_set():
            os.system('cls')
            print(f"{bcolors.WARNING}!!! AT ANYTIME PRESS 'q' to stop mining !!!{bcolors.ENDC}")

            randomResourceGathered = choices(self.items.blocks, self.items.getWeights())[0]['name'] # Choose a random block with its chance being its weight (higher = more likely to get)

            for item in self.resourcesGathered:
                if item['name'] == randomResourceGathered:
                    item['quantity'] += 1

            # This is used to print every gathered
            for resources in self.resourcesGathered:
                if resources['name'] == randomResourceGathered: # To have colored text

                    print(f"{bcolors.BOLD} {resources['name']} gathered x{resources['quantity']} {bcolors.ENDC}")
                else:
                    print(f"{resources['name']} gathered x{resources['quantity']}")
            time.sleep(self.player.miningSpeed)

    def stop(self):
        self._stop.set()

        print(f"\n\n{bcolors.OKGREEN}Total Resources Gathered:{bcolors.ENDC}")
        for resources in self.resourcesGathered:
            print(f"{resources['name']} gathered x{resources['quantity']}")
        time.sleep(1)
        self.player.appendInventory(self.resourcesGathered)
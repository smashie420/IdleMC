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
from shop import Shop
from exceptions import FileNotExistant
from extras.colors import bcolors

# File name for creating/writing/saving data
saveFilename = 'data.json'


# !!! Possible Feature Addition encrypt the data.json with md5 or some other hashing method 
# !!! to prevent players from editing their save
class IdleMC:
    '''
    This is the main class of my game, it contains almost every function, from controlling player data to saving the data
    '''
    def __init__(self):
        self.player = Player()
        
    def initilizeShop(self):
        self.shop = Shop(self.player)

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

    def saveData(self):
        '''
        Saves ALL data (saves IdleMC as a snapshot)
        '''
        if not os.path.exists(saveFilename):
            open(saveFilename, 'a').close()

        self.lastLogin = time.time()
        saveFile = open(saveFilename,'w', encoding="utf-8") 
        saveFile.write(json.dumps(self, default=vars))

    def loadData(self):
        '''
        loads ALL data (restores IdleMC data)
        '''
        if not os.path.exists(saveFilename): # If file doesnt exist then create new one
            saveFile = open(saveFilename,'w', encoding="utf-8") 
            self.player.inventory = IdleMC.blankInventory()
            saveFile.write(json.dumps(self, default=vars))
        
        # Open File and load it into a new player class
        saveFile = open(saveFilename,'r') 
        saveFileDecoded = json.load(saveFile)
        loadedPlayer = Player()

        # Update player class
        for key, value in saveFileDecoded['player'].items():
            setattr(loadedPlayer,key,value)
        self.player = loadedPlayer


    def gatherMaterials(self):
        '''
        This function will start the gathering loop,
            This starts a seperate thread (threadedGoMining) which is the one actually doing the decision making in what gets mined
                THEN IT WILL
            Check for user input on the main thread, if it matches Q kill the mining thread (threadedGoMining)

        '''
        miner = threadedGoMining(self.player)
        thread = threading.Thread(target=miner.start, args=())

        os.system('cls')
        thread.start() # Start the minming thread

        while True:
            event = keyboard.read_event(suppress=True)
            if (event.event_type == keyboard.KEY_DOWN) and event.name == 'q':
                miner.stop()
                break

def print_miner(frame):
        if frame == 0:
            print(
                "                     %%%%%%%%%%%%%%%%                                            \n",
                "                    %%%%%%%%%%%%%%%%         %%%%&&&&&%%%%%                     \n",
                "                    %%//,  @@,,@@  ,               %%%##%%&&%%#@(               \n",
                "                    %%//,,%%////%%,,                   %&&&&%%%%%%              \n",
                "                    ////,,%%%%%%%%,,                  (/*/(@%%%%&&(             \n",
                "               #####(((((((((((((((((((((           #/*/((##%%%&&@%             \n",
                "               #####(((((((((((((((((((((         #/*/(##,     %%%%%            \n",
                "               #####(((((((((((((((((((((      #/*/(##          %%#%            \n",
                "               /////,,,,((((((((((((,,,,,    #/*/(##            %##%            \n",
                "               /////,,,,((((((((((((,,,,, ,(**/(#/              %#@(            \n",
                "               /////,,,,((((((((((((,,,,#/*/(##                                 \n",
                "               /////,,,,((((((((((((,(#/*/(##,                                  \n",
                "               /////,,,,((((((((((#/**/(##                                      \n",
                "                    %%%%####%%%%###/((##                                        \n",
                "                    %%%%####%%%%####                                            \n",
                "                    %%%%####%%%%####                                            \n",
                "                    %%%%####%%%%####                                            \n",
                "                    %%%%####%%%%####                                            \n",
                "                    %%%%####%%%%####                                            \n",
                "                    %%%%####%%%%####                                            \n",
            )
        else:
            print(
                "                     %%%%%%%%%%%%%%%%                                            \n",
                "                    %%%%%%%%%%%%%%%%                                            \n",
                "                    %%//,  @@,,@@  ,                                    ,,,,,,,,\n",
                "                    %%//,,%%////%%,,                                    ,       \n",
                "                    ////,,%%%%%%%%,,                                    ,       \n",
                "               #####(((((((((((((((((((((                               ,       \n",
                "               #####(((((((((((((((((((((                               ,       \n",
                "               #####(((((((((((((((((##(/*/#                            ,       \n",
                "               /////,,,,((((((((((((,,*##(/**#                          ,       \n",
                "               /////,,,,((((((((((((,,,,,/#(/**(,                       ,       \n",
                "               /////,,,,((((((((((((,,,,,   ##(/*/#                 %   ,       \n",
                "               /////,,,,((((((((((((,,,,,     ##(/*/#              %%%%,        \n",
                "               /////,,,,((((((((((((,,,,,        ##(***# ,         %&&%.        \n",
                "                    %%%%####%%%%####               ##(/*/##.      %&&&%,        \n",
                "                    %%%%####%%%%####                 ##(***/#*  .,%%%&%,        \n",
                "                    %%%%####%%%%####                    ###(/*#%&%%#%%*         \n",
                "                    %%%%####%%%%####                 ,..,,*##@%%&&&%%           \n",
                "                    %%%%####%%%%####                *    #%%%%%%%##%,,          \n",
                "                    %%%%####%%%%####            %%%%%%@%%%%&&&%%%%((            \n",
                "                    %%%%####%%%%####        ,  .%@####%%%%%%%%                  \n",
        )
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
        frame = 0
        while not self._stop.is_set():
            os.system('cls')

            if frame > 1: # This is for the little animation of steve mining
                frame = 0
            print_miner(frame)

            print(f"{bcolors.WARNING}!!! AT ANYTIME PRESS 'q' to stop mining !!!{bcolors.ENDC}")
            randomResourceGathered = choices(self.items.blocks, self.items.getWeights())[0]['name'] # Choose a random block with its chance being its weight (higher = more likely to get)

            for item in self.resourcesGathered:
                if item['name'] == randomResourceGathered:
                    item['quantity'] += 1 # Possibly add an player upgrade to get a resource gathered multiplier

            # This is used to print every gathered
            for resources in self.resourcesGathered:
                if resources['name'] == randomResourceGathered: # To have colored text
                    print(f"{bcolors.BOLD} {resources['name']} gathered x{resources['quantity']} {bcolors.ENDC}")
                else:
                    print(f"{resources['name']} gathered x{resources['quantity']}")

            if len(self.player.upgrades) > 0: # Check if player has any upgrades
                # Gets the best tool and uses that miningSpeed * playersMining Speed
                time.sleep(self.player.miningSpeed * self.player.upgrades[len(self.player.upgrades)-1]['miningSpeed'])
            else:
                time.sleep(self.player.miningSpeed)
            frame += 1

    def stop(self):
        self._stop.set()

        print(f"\n\n{bcolors.OKGREEN}Total Resources Gathered:{bcolors.ENDC}")
        for resources in self.resourcesGathered:
            print(f"{resources['name']} gathered x{resources['quantity']}")
        print("\n")
        time.sleep(1)
        self.player.appendInventory(self.resourcesGathered)
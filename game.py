# Used to serialize and decode json and used to detect if savefile exists
import json
import os

# Used for sleeping (gatherMaterials)
import time
# Used for random rolls (gatherMaterials)
from random import randint
# Used to detect if a key is pressed (gatherMaterials)
import keyboard
# Used for mining
import threading

# Imports from files i've created:
from exceptions import FileNotExistant
from extras.colors import bcolors

# File name for creating/writing/saving data
saveFilename = 'data.json'


# !!! Possible Feature Addition encrypt the data.json with md5 or some other hashing method 
# !!! to prevent players from editing their save
class IdleMC:
    def __init__(self):
        self.lastRecDate = ''
        self.currentDate = ''


    def gatherMaterials(self, player):
        miner = threadedGoMining(player)
        thread = threading.Thread(target=miner.start, args=())

        print(f"{bcolors.WARNING}!!! AT ANYTIME PRESS 'q' to stop mining !!!{bcolors.ENDC}")
        time.sleep(2)
        thread.start()

        while True:
            if keyboard.read_key('q'):
                miner.stop()
                break

    def saveData(self):
        if not os.path.exists(saveFilename):
            open(saveFilename, 'a').close()
        saveFile = open(saveFilename,'w', encoding="utf-8") 
        saveFile.write(json.dumps(self, default=vars))

    def loadData(self):
        if not os.path.exists(saveFilename):
            raise FileNotExistant
        saveFile = open(saveFilename,'r') 

        saveFileDecoded = json.load(saveFile)

        for key, value in saveFileDecoded.items():
            setattr(self,key,value)

'''
This class is used in "IdleMC" class for method gatherMaterials()
'''
class threadedGoMining:
    def __init__(self, player):
        self._stop = threading.Event()
        self.player = player

    def start(self):
        time.sleep(0.1)
        while not self._stop.is_set():
            rollDice = randint(0,1)
            print(f"ROLLED: {rollDice}")

            time.sleep(self.player.miningDelay)
            

    def stop(self):
        self._stop.set()


# Used to serialize and decode json and used to detect if savefile exists
import json
import os
import time

# Used for mining and waiting for input at the same time
import threading

from exceptions import FileNotExistant

DataFileName = 'data.json'

# !!! Possible Feature Addition encrypt the data.json with md5 or some other hashing method 
# !!! to prevent players from editing their save


class Player:
    def __init__(self):
        self.minecoins = 0
        
        self.miningSpeed = 1
        self.miningDelay = 1

        self.upgrades = []

    def gatherMaterials(self):
        loop = threadedGoMining(self)
        thread = threading.Thread(target=loop.start)

        try:
            thread.start()

            while True:
                inp = input("!!! AT ANYTIME TYPE 'q' to stop mining !!!\n")
                if inp.lower() == "q":
                    loop.stop()
                    break

        except KeyboardInterrupt:
            print("KeyboardInterrupt: Stopping the loop...")
            loop.stop()

        
    
    def saveData(self):
        if not os.path.exists(DataFileName):
            open(DataFileName, 'a').close()
        saveFile = open(DataFileName,'w') 
        saveFile.write(json.dumps(self, default=vars))

    def loadData(self):
        if not os.path.exists(DataFileName):
            raise FileNotExistant
        saveFile = open(DataFileName,'r') 

        saveFileDecoded = json.load(saveFile)

        for key, value in saveFileDecoded.items():
            setattr(self,key,value)

        


'''
This class is used in "Player" class for method gatherMaterials()
'''
class threadedGoMining:
    def __init__(self, player):
        self._stop = threading.Event()
        self.player = player

    def start(self):
        time.sleep(0.1)
        while not self._stop.is_set():
            print("Looping...")
            time.sleep(self.player.miningDelay)

    def stop(self):
        self._stop.set()

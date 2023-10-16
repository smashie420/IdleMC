# Used to serialize and decode json and used to detect if savefile exists
import json
import os

from exceptions import FileNotExistant

DataFileName = 'data.json'

# !!! Possible Feature Addition encrypt the data.json with md5 or some other hashing method 
# !!! to prevent players from editing their save


class Player:
    def __init__(self):
        self.minecoins = 0
        self.upgrades = []
    
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

        
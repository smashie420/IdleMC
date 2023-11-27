from exceptions import BlockNotExistant

class Items:
    def __init__(self):
        self.blocks = {
            0: {
                "name": "Dirt",
                "worth": 1,
                "weight": 100
            },
            1: {
                "name": "Cobblestone",
                "worth": 5,
                "weight": 50
            }, 
            2: {
                "name": "Coal",
                "worth": 10,
                "weight": 30
            },
            3: {
                "name": "Iron",
                "worth": 25,
                "weight": 30
            },
            4: {
                "name": "Gold",
                "worth": 50,
                "weight": 20
            },
            5: {
                "name": "Diamond",
                "worth": 100,
                "weight": 10
            },
        }

        self.items = {
            0: {
                "name": "Wooden Pickaxe",
                "price": 100,
                "miningSpeed": 0.80
            },
            1: {
                "name": "Stone Pickaxe",
                "price": 200,
                "miningSpeed": 0.75
            },
            2: {
                "name": "Iron Pickaxe",
                "price": 1000,
                "miningSpeed": 0.50
            },
            2: {
                "name": "Gold Pickaxe",
                "price": 2000,
                "miningSpeed": 0.35
            },
            3: {
                "name": "Diamond Pickaxe",
                "price": 10000,
                "miningSpeed": 0.20
            },
            4: {
                "name": "Netherite Pickaxe",
                "price": 100000,
                "miningSpeed": 0.05
            },
        }
    
    def getWeights(self):
        '''
        Returns an array of weights of each item
        '''
        weights = list([])
        for i in range(len(self.blocks)):
            weights.append(self.blocks[i]['weight'])
        return weights

    def getBlocks(self):
        '''
        Returns an array of all blocks
        '''
        blocks = list([])
        for i in range(len(self.blocks)):
            blocks.append(self.blocks[i]['name'])
        return blocks

    def getWorth(self, block_name):
        '''
        Searches for the weight of a block by giving an input of a block name
        '''
        for i in range(len(self.blocks)):
            if block_name == self.blocks[i]['name']:
                return self.blocks[i]['worth']
        # Returns raise exception
        raise BlockNotExistant()
    
    def getItemWorth(self, item_name):
        '''
        Searches for the weight of a block by giving an input of a block name
        '''
        
        for i in range(len(self.items)):
            if item_name == self.items[i]['name']:
                return self.items[i]['price']
        # Returns raise exception
        raise BlockNotExistant()
    
    def getItem(self, item_name):
        '''
        Returns the data corresponding to the items name
        EX:
            getItem("Wooden Pickaxe")

            RETURNS
            {"name": "Wooden Pickaxe","price": 100,"miningSpeed": 0.80}
        '''
        for i in range(len(self.items)):
            if item_name == self.items[i]['name']:
                return self.items[i]
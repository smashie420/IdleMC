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
    
    def getWeights(self):
        '''
        Returns an array of weights of each item
        '''
        weights = list([])
        for i in range(len(self.blocks)):
            weights.append(self.blocks[i]['weight'])
        return weights

    def getBlocks(self):
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



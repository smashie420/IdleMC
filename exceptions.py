from extras.colors import bcolors

class FileNotExistant(Exception):
    def __init__(self, message=f'{bcolors.WARNING}File isn\'t found\nCheck formatting!{bcolors.ENDC}'):
        self.message = message
        super().__init__(self.message)

class BlockNotExistant(Exception):
    def __init__(self, message=f'{bcolors.WARNING}Block isn\'t found in block list! Check spelling!{bcolors.ENDC}'):
        self.message = message
        super().__init__(self.message)
        #self.value = f'Block isn\'t found in block list!\n {bcolors.WARNING}Check spelling!{bcolors.ENDC}'

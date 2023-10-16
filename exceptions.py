class FileNotExistant(Exception):
    def __init__(self):
        self.value = 'File isn\'t found\nCheck formatting!\n'
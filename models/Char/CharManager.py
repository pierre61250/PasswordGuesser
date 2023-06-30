import string

class CharManager():
    def __init__(self):
        self.__char = [".","$","?","!","*"]
        self.__allChar = list(string.punctuation)

    @property
    def char(self):
        return self.__char
    
    @property
    def allChar(self):
        return self.__allChar
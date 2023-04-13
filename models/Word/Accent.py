from .WordManager import WordManager
from unidecode import unidecode

class Accent(WordManager):

    def __init__(self, words):
        super().__init__(words)

    def transform(self):
        result = []
        for word in self.words:
            result.append(unidecode(word))
        return result
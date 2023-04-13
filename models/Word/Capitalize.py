from .WordManager import WordManager

class Capitalize(WordManager):

    def __init__(self, words):
        super().__init__(words)

    def transform(self):
        result = []
        for word in self.words:
            result.append(word.capitalize())
        return result
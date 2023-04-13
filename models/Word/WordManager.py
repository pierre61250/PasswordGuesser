from abc import abstractmethod

class WordManager():
    @abstractmethod
    def __init__(self, words):
        self.words = words
        self.possibilities = self.run()

    def run(self):
        # Lance la methode de transformation
        return self.transform()

    def transform(self):
        return [];
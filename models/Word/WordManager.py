from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def transform(self):
        pass

class WordManager(Interface):
    @abstractmethod
    def __init__(self, words):
        self.__words = words
        self.possibilities = self.run()

    @property
    def words(self):
        return self.__words

    def run(self):
        # Lance la methode de transformation
        return self.transform()

    def transform(self):
        return [];
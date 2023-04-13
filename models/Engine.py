from itertools import combinations, permutations
from .Word.Capitalize import Capitalize
from .Word.Uppercase import Uppercase
from .Word.Lowercase import Lowercase
from .Word.Accent import Accent
from .Word.Leet import Leet

class Engine:

    def __init__(self, words, options = []):
        self.words = words
        self.options = options
        self.possibilities = []
        self.passwords = self.run()

    def run(self):
        if 'upper' in self.options:
            self.updateWords(Uppercase(self.words).possibilities)
        if 'lower' in self.options:
            self.updateWords(Lowercase(self.words).possibilities)
        if 'capitalize' in self.options:
            self.updateWords(Capitalize(self.words).possibilities)
        if 'accent' in self.options:
            self.updateWords(Accent(self.words).possibilities)
        if 'leet' in self.options:
            self.updateWords(Leet(self.words).possibilities)

        print(self.words)

        # Mets en place toutes les combinaisons
        self.permute_and_combine_list()
        # Créer une list avec toutes les combinaisons sous forme de string
        return self.fromArrayToString()
    
    def updateWords(self, newWords):
        self.words = list(set(self.words + newWords))

    def permute_and_combine_list(self):
        """
        Permute et combine les éléments de la liste donnée en utilisant les méthodes
        permutations et combinations de la bibliothèque itertools et retourne une liste de
        toutes les permutations et combinaisons possibles.
        """
        limit = 6 if len(self.words) > 5 else len(self.words)+1
        for i in range(1, limit):
            # génère toutes les combinaisons de longueur i
            for combo in combinations(self.words, i):
                # génère toutes les permutations pour chaque combinaison
                for perm in permutations(combo):
                    self.possibilities.append(perm)
    
    def fromArrayToString(self):
        result = []
        for item in self.possibilities:
            result.append(''.join(item))
        return result
from .WordManager import WordManager

class Leet(WordManager):

    leetList = {
        'a': '4',
        'b': '8',
        'e': '3',
        'i': '1',
        'o': '0',
        'l': '1',
        's': '5',
        't': '7',
        'z': '2',
        'g': '6'
    }

    def __init__(self, words):
        super().__init__(words)

    def toLeet(self):
        result = []
        for word in self.words:
            leet_text = ''
            for char in word:
                leet_text += self.leetList.get(char.lower(), char)
            result.append(leet_text)
        return result
    
    def transform(self):
        return self.toLeet()
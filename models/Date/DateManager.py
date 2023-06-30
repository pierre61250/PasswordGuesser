from datetime import datetime

class DateManager():
    months_english = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    months_french = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    
    def __init__(self, date):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.possibilities = self.run()

    @staticmethod
    def isDate(date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def run(self):
        # Lance la methode de transformation
        return self.transform()
    
    @staticmethod
    def transformToFrench(month):
        if month in DateManager.months_english:
            index = DateManager.months_english.index(month)
            return DateManager.months_french[index]
    
    def numberToLetter(self):
        month = self.date.strftime("%B");
        return [month, self.transformToFrench(month)]
    
    def dateDecomposition(self):
        return [self.date.strftime("%m"), self.date.strftime("%d"), self.date.strftime("%Y"), str(self.date.month), str(self.date.day), self.date.strftime("%y")]

    def transform(self):
        return self.numberToLetter() + self.dateDecomposition();
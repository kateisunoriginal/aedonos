
class Year:
    def __init__(self, startingYear):
        self.selfYear = 0
        self.startingYear = startingYear
    def getCurrentYear(self):
        return self.selfYear
    def incrementYear(self):
        self.selfYear += 1
    def getAbsoluteYear(self):
        return self.selfYear+self.startingYear

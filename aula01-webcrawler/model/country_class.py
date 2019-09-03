class Country:
    name=""
    capital=""
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
    
    def printCountry(self):
        print("None: " + str(self.name) + ' --> ' + "Capital: " + str(self.capital))
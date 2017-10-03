
class City():


    def __init__(self, _name):
        self.name = _name
        self.adjacentCities = []

    def addAdjacent(self,city,distance):
        self.adjacentCities.append((city,distance))

from core import SolutionAdapter
from core.DistancePOI import DistancePOI
from core.Problem import Problem
from test.CityProblem.City import City


class SimpleCityProblem(Problem):

    cities = []
    city_names = ["A","B","C","D","E","F","G","H","I","J"]

    def __init__(self, _startCity, _endCity, _distance:DistancePOI, _solAdapter: SolutionAdapter):
        self.startCity = _startCity
        self.endCity = _endCity
        self.distance = _distance
        self.solutionAdapter = _solAdapter
        self.start_state = (self.startCity, 0)
        self.unique_successors = False
        self.CreateCitiesGraph()  # genera il grafo delle citta


    def CreateCitiesGraph(self):
        # creare le citta
        for c in self.city_names:
            ct = City(c)
            self.cities.append(ct)

        cc = next((x for x in self.cities if x.name == "A"), None)
        cc.addAdjacent("C", 10)
        cc.addAdjacent("B", 10)
        cc = next((x for x in self.cities if x.name == "B"), None)
        cc.addAdjacent("A", 10)
        cc.addAdjacent("D", 10)
        cc.addAdjacent("E", 10)
        cc = next((x for x in self.cities if x.name == "C"), None)
        cc.addAdjacent("A", 10)
        cc.addAdjacent("F", 10)
        cc.addAdjacent("E", 10)
        cc = next((x for x in self.cities if x.name == "D"), None)
        cc.addAdjacent("B", 10)
        cc.addAdjacent("G", 5)
        cc = next((x for x in self.cities if x.name == "E"), None)
        cc.addAdjacent("B", 10)
        cc.addAdjacent("C", 10)
        cc.addAdjacent("H", 10)
        cc.addAdjacent("I", 10)
        cc = next((x for x in self.cities if x.name == "F"), None)
        cc.addAdjacent("I", 10)
        cc.addAdjacent("C", 10)
        cc = next((x for x in self.cities if x.name == "G"), None)
        cc.addAdjacent("D", 5)
        cc.addAdjacent("J", 5)
        cc = next((x for x in self.cities if x.name == "H"), None)
        cc.addAdjacent("J", 10)
        cc.addAdjacent("G", 10)
        cc.addAdjacent("E", 10)
        cc = next((x for x in self.cities if x.name == "I"), None)
        cc.addAdjacent("E", 10)
        cc.addAdjacent("F", 10)
        cc.addAdjacent("J", 20)
        cc = next((x for x in self.cities if x.name == "J"), None)
        cc.addAdjacent("G", 5)
        cc.addAdjacent("I", 20)

    def goal(self, state):
        return state[0] == self.endCity


    def h(self, path):
        result = 1
        return (result,)


    def g(self, path):
        result = 0
        if len(path) == 1:
            result = 0
        else:
            index = 1
            for index in range(1, len(path)):
                (city, cost) = path[index]
                result = result + cost

        if self.distance is not None:
            adaptedSolution = self.solutionAdapter.AdaptAStarSolution(path)
            secondLevelCost = self.distance.getDistance(adaptedSolution)
            return result, secondLevelCost
        else:
            return (result,)


    def successors(self, state):
        nextCities = []
        city = next((x for x in self.cities if x.name == state[0]), None)
        for c in city.adjacentCities:
            nextCities.append(c)
        return nextCities
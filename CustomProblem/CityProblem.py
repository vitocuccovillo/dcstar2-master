from CustomProblem.City import City
from test.Problem import Problem
from test.DistancePOI import DistancePOI
from test.SolutionAdapter import SolutionAdapter

class CityProblem(Problem):

    city_names = ["Arad", "Oradea", "Zerind", "Sibiu", "Timisoara", "Lugoj", "Mehadia",
                  "Drobeta", "Craiova", "Rimnicu Vilcea", "Fagaras", "Bucarest", "Pitesti",
                  "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Vaslui", "Iasi", "Neamt"]

    cities = []


    def __init__(self, _startCity, _endCity, _distance:DistancePOI, _solAdapter:SolutionAdapter):

        self.startCity = _startCity
        self.endCity = _endCity
        self.distance = _distance
        self.solutionAdapter = _solAdapter
        self.start_state = (self.startCity,0)
        self.unique_successors = False
        self.CreateCitiesGraph()


    #PROBLEM ABSTRACT METHODS IMPLEMENTATION

    def goal(self, path):
        pathLen = len(path)
        return path[0] == self.endCity

    def g(self, path):
        result = 0
        if len(path) == 1:
            result = 0
        else:
            index = 1
            for index in range(1,len(path)):
                (city,cost) = path[index]
                result = result + cost

        if self.distance is not None:
            adaptedSolution = self.solutionAdapter.AdaptAStarSolution(path)
            secondLevelCost = self.distance.getDistance(adaptedSolution)
            return result, secondLevelCost
        else:
            return (result,)

    def h(self, path):
        #una semplice euristica: se una città è ripetuta nel path assegno un costo di 100
        # altrimenti assegno 10, cerco di evitare i loop
        result = 0
        return (result,)
        # count = 0
        # if len(path) == 1:
        #     result = 1
        # else:
        #     lastCity = path[len(path)-1][0]
        #     for index in range(0,len(path)):
        #         if path[index][0] == lastCity:
        #             count += 1
        #     if count == 1:
        #         result = 1
        #     else:
        #         result = 100*count + len(path)
        # return result, 0

    def successors(self, state):
        nextCities = []
        city = next((x for x in self.cities if x.name == state[0]), None)
        for c in city.adjacentCities:
            nextCities.append(c)
        return nextCities


    # END PROBLEM IMPL

    def getCities(self):
        return self.cities

    def CreateCitiesGraph(self):
        # creare le citta
        for c in self.city_names:
            ct = City(c)
            self.cities.append(ct)

        # crea il grafo
        cc = next((x for x in self.cities if x.name == "Arad"), None)
        cc.addAdjacent("Zerind", 75)
        cc.addAdjacent("Sibiu", 140)
        cc.addAdjacent("Timisoara", 118)

        cc = next((x for x in self.cities if x.name == "Timisoara"), None)
        cc.addAdjacent("Arad", 118)
        cc.addAdjacent("Lugoj", 140)

        cc = next((x for x in self.cities if x.name == "Lugoj"), None)
        cc.addAdjacent("Timisoara", 111)
        cc.addAdjacent("Mehadia", 70)

        cc = next((x for x in self.cities if x.name == "Mehadia"), None)
        cc.addAdjacent("Drobeta", 75)
        cc.addAdjacent("Lugoj", 70)

        cc = next((x for x in self.cities if x.name == "Zerind"), None)
        cc.addAdjacent("Arad", 75)
        cc.addAdjacent("Oradea", 71)

        cc = next((x for x in self.cities if x.name == "Oradea"), None)
        cc.addAdjacent("Sibiu", 151)
        cc.addAdjacent("Zerind", 71)

        cc = next((x for x in self.cities if x.name == "Sibiu"), None)
        cc.addAdjacent("Arad", 140)
        cc.addAdjacent("Oradea", 151)
        cc.addAdjacent("Fagaras", 99)
        cc.addAdjacent("Rimnicu Vilcea", 80)

        cc = next((x for x in self.cities if x.name == "Rimnicu Vilcea"), None)
        cc.addAdjacent("Pitesti", 97)
        cc.addAdjacent("Craiova", 146)
        cc.addAdjacent("Sibiu", 80)

        cc = next((x for x in self.cities if x.name == "Drobeta"), None)
        cc.addAdjacent("Mehadia", 75)
        cc.addAdjacent("Craiova", 120)

        cc = next((x for x in self.cities if x.name == "Craiova"), None)
        cc.addAdjacent("Pitesti", 138)
        cc.addAdjacent("Drobeta", 120)
        cc.addAdjacent("Rimnicu Vilcea", 146)

        cc = next((x for x in self.cities if x.name == "Fagaras"), None)
        cc.addAdjacent("Sibiu", 99)
        cc.addAdjacent("Bucarest", 211)

        cc = next((x for x in self.cities if x.name == "Bucarest"), None)
        cc.addAdjacent("Giurgiu", 90)
        cc.addAdjacent("Fagaras", 211)
        cc.addAdjacent("Pitesti", 101)
        cc.addAdjacent("Urziceni", 85)

        cc = next((x for x in self.cities if x.name == "Pitesti"), None)
        cc.addAdjacent("Rimnicu Vilcea", 97)
        cc.addAdjacent("Craiova", 138)
        cc.addAdjacent("Bucarest", 101)

        cc = next((x for x in self.cities if x.name == "Urziceni"), None)
        cc.addAdjacent("Hirsova", 98)
        cc.addAdjacent("Vaslui", 142)
        cc.addAdjacent("Bucarest", 85)

        cc = next((x for x in self.cities if x.name == "Hirsova"), None)
        cc.addAdjacent("Urziceni", 98)
        cc.addAdjacent("Eforie", 86)

        cc = next((x for x in self.cities if x.name == "Vaslui"), None)
        cc.addAdjacent("Urziceni", 142)
        cc.addAdjacent("Iasi", 92)

        cc = next((x for x in self.cities if x.name == "Iasi"), None)
        cc.addAdjacent("Neamt", 87)
        cc.addAdjacent("Vaslui", 92)

        cc = next((x for x in self.cities if x.name == "Neamt"), None)
        cc.addAdjacent("Iasi", 87)

        cc = next((x for x in self.cities if x.name == "Eforie"), None)
        cc.addAdjacent("Hirsova", 86)

        cc = next((x for x in self.cities if x.name == "Giurgiu"), None)
        cc.addAdjacent("Bucarest", 90)
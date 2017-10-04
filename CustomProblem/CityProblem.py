from CustomProblem.City import City
from test.Problem import Problem
from test.DistancePOI import DistancePOI
from test.SolutionAdapter import SolutionAdapter

class CityProblem(Problem):

    cities = []
    city_names = ["Arad", "Oradea", "Zerind", "Sibiu", "Timisoara", "Lugoj", "Mehadia",
                  "Drobeta", "Craiova", "Rimnicu Vilcea", "Fagaras", "Bucarest", "Pitesti",
                  "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Vaslui", "Iasi", "Neamt"]
    distancesMatrix = [[0,60,40,90,60,100,130,160,200,130,160,260,200,270,290,340,380,310,290,240],
                    [60,0,40,110,120,150,180,200,230,140,160,270,210,290,290,340,380,300,260,200],
                    [40,40,0,90,100,120,150,180,210,130,160,260,200,280,290,340,380,300,270,220],
                    [90,110,90,0,90,60,90,120,130,40,70,170,100,180,200,260,290,220,200,160],
                    [60,120,100,90,0,60,70,100,150,100,160,230,170,230,270,330,360,310,290,250],
                    [100,150,120,60,60,0,40,60,90,60,120,180,120,180,220,270,300,260,250,220],
                    [130,180,150,90,70,40,0,40,70,80,140,180,120,160,220,270,300,270,260,230],
                    [160,200,180,120,100,60,40,0,60,100,160,180,120,160,220,280,300,280,280,250],
                    [200,230,210,130,150,90,70,60,0,300,120,120,80,90,160,220,230,230,240,220],
                    [130,140,130,40,100,60,80,100,300,0,60,140,70,140,170,230,260,200,200,160],
                    [160,160,160,70,160,120,140,160,120,60,0,120,260,140,130,180,220,150,130,100],
                    [260,270,260,170,230,180,180,180,120,140,120,0,70,50,40,100,120,120,150,160],
                    [200,210,200,100,170,120,120,120,80,70,260,70,0,80,100,160,190,160,150,140],
                    [270,290,280,180,230,180,160,160,90,140,140,50,80,0,80,120,140,160,200,200],
                    [290,290,290,200,270,220,220,220,160,170,130,40,100,80,0,60,80,80,120,140],
                    [340,340,340,260,330,270,270,280,220,230,180,100,160,120,60,0,250,80,120,170],
                    [380,380,380,290,360,300,300,300,230,260,220,120,190,140,80,250,0,120,180,220],
                    [310,300,300,220,310,260,270,280,230,200,150,120,160,160,80,80,120,0,60,100],
                    [290,260,270,200,290,250,260,280,240,200,130,150,150,200,120,120,180,60,0,60],
                    [240,200,220,160,250,220,230,250,220,160,100,160,140,200,140,170,220,100,60,0]]



    def __init__(self, _startCity, _endCity, _distance:DistancePOI, _solAdapter:SolutionAdapter):

        self.startCity = _startCity
        self.endCity = _endCity
        self.distance = _distance
        self.solutionAdapter = _solAdapter
        self.start_state = (self.startCity,0)
        self.unique_successors = False
        self.CreateCitiesGraph() #genera il grafo delle citta


    #PROBLEM ABSTRACT METHODS IMPLEMENTATION

    def goal(self, state):
        return state[0] == self.endCity

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

    def h(self, path): #uso come euristica la distanza euclidea della citta corrente dalla finale
        cityIndex = self.city_names.index(path[-1][0])
        endCityIndex = self.city_names.index(self.endCity)
        cost = self.distancesMatrix[cityIndex][endCityIndex]
        return (cost,len(path))


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
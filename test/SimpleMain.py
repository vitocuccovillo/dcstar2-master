import random

import time

from test.CityProblem.City import City

from GAGuide.InspyredImpl import InspyredImpl
from core.DistancePOI import DistancePOI
from core.Problem import Problem
from core.SolutionAdapter import SolutionAdapter
from core.heuristic_search.astar import astar
from test.CityProblem.SimpleCityProblem2 import SimpleCityProblem2
from test.LevenshteinDistance import levenshtein

class SimpleMain():

    cities = []
    #city_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    city_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V"]
    start_city = "A"
    end_city = "U"

#---------- FUNCTIONS ---------------
    # def CreateCitiesGraph(self):
    #     # creare le citta
    #     for c in self.city_names:
    #         ct = City(c)
    #         self.cities.append(ct)
    #
    #     cc = next((x for x in self.cities if x.name == "A"), None)
    #     cc.addAdjacent("C", 10)
    #     cc.addAdjacent("B", 10)
    #     cc = next((x for x in self.cities if x.name == "B"), None)
    #     cc.addAdjacent("A", 10)
    #     cc.addAdjacent("D", 10)
    #     cc.addAdjacent("E", 10)
    #     cc = next((x for x in self.cities if x.name == "C"), None)
    #     cc.addAdjacent("A", 10)
    #     cc.addAdjacent("F", 10)
    #     cc.addAdjacent("E", 10)
    #     cc = next((x for x in self.cities if x.name == "D"), None)
    #     cc.addAdjacent("B", 10)
    #     cc.addAdjacent("G", 5)
    #     cc = next((x for x in self.cities if x.name == "E"), None)
    #     cc.addAdjacent("B", 10)
    #     cc.addAdjacent("C", 10)
    #     cc.addAdjacent("H", 10)
    #     cc.addAdjacent("I", 10)
    #     cc = next((x for x in self.cities if x.name == "F"), None)
    #     cc.addAdjacent("I", 10)
    #     cc.addAdjacent("C", 10)
    #     cc = next((x for x in self.cities if x.name == "G"), None)
    #     cc.addAdjacent("D", 5)
    #     cc.addAdjacent("J", 5)
    #     cc = next((x for x in self.cities if x.name == "H"), None)
    #     cc.addAdjacent("J", 10)
    #     cc.addAdjacent("G", 10)
    #     cc.addAdjacent("E", 10)
    #     cc = next((x for x in self.cities if x.name == "I"), None)
    #     cc.addAdjacent("E", 10)
    #     cc.addAdjacent("F", 10)
    #     cc.addAdjacent("J", 20)
    #     cc = next((x for x in self.cities if x.name == "J"), None)
    #     cc.addAdjacent("G", 5)
    #     cc.addAdjacent("I", 20)
    def CreateCitiesGraph(self):
        # creare le citta
        for c in self.city_names:
            ct = City(c)
            self.cities.append(ct)

        cc = next((x for x in self.cities if x.name == "A"), None)
        cc.addAdjacent("C", 10)
        cc.addAdjacent("B", 10)
        cc.addAdjacent("K", 10)
        cc = next((x for x in self.cities if x.name == "B"), None)
        cc.addAdjacent("A", 10)
        cc.addAdjacent("D", 10)
        cc.addAdjacent("E", 10)
        cc.addAdjacent("K", 10)
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
        cc.addAdjacent("N", 10)
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
        cc.addAdjacent("T", 10)
        cc = next((x for x in self.cities if x.name == "J"), None)
        cc.addAdjacent("G", 5)
        cc.addAdjacent("I", 20)
        cc.addAdjacent("M", 10)
        cc.addAdjacent("T", 10)
        cc.addAdjacent("V", 5)
        cc = next((x for x in self.cities if x.name == "K"), None)
        cc.addAdjacent("A", 10)
        cc.addAdjacent("B", 10)
        cc.addAdjacent("L", 10)
        cc = next((x for x in self.cities if x.name == "L"), None)
        cc.addAdjacent("K", 10)
        cc.addAdjacent("M", 10)
        cc = next((x for x in self.cities if x.name == "M"), None)
        cc.addAdjacent("L", 10)
        cc.addAdjacent("J", 10)
        cc = next((x for x in self.cities if x.name == "N"), None)
        cc.addAdjacent("F", 10)
        cc.addAdjacent("O", 5)
        cc = next((x for x in self.cities if x.name == "O"), None)
        cc.addAdjacent("N", 10)
        cc.addAdjacent("P", 10)
        cc.addAdjacent("Q", 5)
        cc = next((x for x in self.cities if x.name == "P"), None)
        cc.addAdjacent("O", 10)
        cc.addAdjacent("R", 5)
        cc = next((x for x in self.cities if x.name == "Q"), None)
        cc.addAdjacent("O", 5)
        cc.addAdjacent("S", 10)
        cc = next((x for x in self.cities if x.name == "R"), None)
        cc.addAdjacent("P", 5)
        cc.addAdjacent("T", 10)
        cc = next((x for x in self.cities if x.name == "S"), None)
        cc.addAdjacent("Q", 10)
        cc.addAdjacent("U", 5)
        cc = next((x for x in self.cities if x.name == "T"), None)
        cc.addAdjacent("R", 10)
        cc.addAdjacent("I", 10)
        cc.addAdjacent("J", 10)
        cc = next((x for x in self.cities if x.name == "U"), None)
        cc.addAdjacent("S", 5)
        cc.addAdjacent("V", 20)
        cc = next((x for x in self.cities if x.name == "V"), None)
        cc.addAdjacent("J", 5)
        cc.addAdjacent("U", 20)

    def generate(rndm, args):
        startIndex = SimpleMain.city_names.index(SimpleMain.start_city)
        individual = [0]*len(SimpleMain.city_names) #individuo è un array di n elementi, ho 0 se non passo dalla citta, i altrimenti
        individual[startIndex] = 1
        newCity = SimpleMain.start_city
        i = 1
        while newCity != SimpleMain.end_city:
            city: City = next((x for x in SimpleMain.cities if x.name == newCity), None)
            succIndex = random.randint(0,len(city.adjacentCities)-1)
            succCity = city.adjacentCities[succIndex][0]
            newCity = succCity
            cityIndex = SimpleMain.city_names.index(succCity)
            if individual[cityIndex] == 0: #se non sono mai passato da questa città la aggiunge al path
                i += 1
                individual[cityIndex] = i
        return individual


    def evaluate(individual, args):
        fitness = 10000
        if SimpleMain.city_names[individual.index(1)] == SimpleMain.start_city and SimpleMain.city_names[individual.index(max(individual))] == SimpleMain.end_city:
            try:
                i = 1
                cityIndex = individual.index(i)
                cityName = SimpleMain.city_names[cityIndex]
                while cityName != SimpleMain.end_city:
                    city: City = next((x for x in SimpleMain.cities if x.name == cityName), None)
                    i+=1
                    cityIndex = individual.index(i)
                    cityName = SimpleMain.city_names[cityIndex]
                    cc =  next((x for x in city.adjacentCities if x[0] == cityName), None)
                    if cc is None:
                        fitness = 5000
                        break
                    else:
                        (c,cost) = cc
                        fitness += cost
            except:
                pass
        return -fitness

#END FUNCTIONS ----------------------


if __name__ == '__main__':

    # ----------- INIZIO -----------------

    numIterations = 20
    avgExpansions = 0

    for i in range(0,numIterations):

        simpleMain = SimpleMain();
        simpleMain.CreateCitiesGraph()
        inspyredWp = InspyredImpl(SimpleMain.generate,SimpleMain.evaluate) # genera una soluzione con il GA
        genetic_sols = inspyredWp.getBestIndividuals(max_evaluations=200,
                                                     num_elites=1,
                                                     mutation_rate=0.1,
                                                     pop_size=10)
        bestIndividual = genetic_sols[0]
        solAdapter = SolutionAdapter(simpleMain.city_names)
        bestGASol = solAdapter.AdaptGASolution(bestIndividual)

        #bestGASol = ["A","C","F","I","E","I","H","J"]
        #bestGASol = ["A","B","D","G","H","J"]
        print("SOLUZIONE ALGORITMO GENETICO: " + str(bestGASol))

        dist = DistancePOI(bestGASol,levenshtein) # genera un oggetto DistancePoi prendendo in input la soluz. del GA ed una funzione

        cp:Problem = SimpleCityProblem2(SimpleMain.start_city,SimpleMain.end_city,dist,solAdapter) # costruisco il problema (fornisco in input le città e l'oggetto dist)
        #cp = SimpleCityProblem2(SimpleMain.start_city,SimpleMain.end_city,None, solAdapter) # costruisco il problema (fornisco in input le città e l'oggetto dist)
        (solution,numExpansions) = astar(cp)
        avgExpansions = avgExpansions + numExpansions
        print("SOLUZIONE A*:" + str(solution))
        print("------------------------------")

    print("")
    print("MEDIA ESPANSIONI: " + str(avgExpansions / numIterations))
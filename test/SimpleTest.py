from CustomProblem.SimpleCityProblem import SimpleCityProblem
from heuristic_search.astar import astar
from test.DistancePOI import DistancePOI
from test.InspyredImpl import InspyredImpl
from test.LevenshteinDistance import levenshtein
from test.SolutionAdapter import SolutionAdapter
from CustomProblem.City import City
import random

cities = []
city_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
start_city = "A"
end_city = "J"


def CreateCitiesGraph():
    # creare le citta
    for c in city_names:
        ct = City(c)
        cities.append(ct)

    cc = next((x for x in cities if x.name == "A"), None)
    cc.addAdjacent("C", 10)
    cc.addAdjacent("B", 10)
    cc = next((x for x in cities if x.name == "B"), None)
    cc.addAdjacent("A", 10)
    cc.addAdjacent("D", 10)
    cc.addAdjacent("E", 10)
    cc = next((x for x in cities if x.name == "C"), None)
    cc.addAdjacent("A", 10)
    cc.addAdjacent("F", 10)
    cc.addAdjacent("E", 10)
    cc = next((x for x in cities if x.name == "D"), None)
    cc.addAdjacent("B", 10)
    cc.addAdjacent("G", 5)
    cc = next((x for x in cities if x.name == "E"), None)
    cc.addAdjacent("B", 10)
    cc.addAdjacent("C", 10)
    cc.addAdjacent("H", 10)
    cc.addAdjacent("I", 10)
    cc = next((x for x in cities if x.name == "F"), None)
    cc.addAdjacent("I", 10)
    cc.addAdjacent("C", 10)
    cc = next((x for x in cities if x.name == "G"), None)
    cc.addAdjacent("D", 5)
    cc.addAdjacent("J", 5)
    cc = next((x for x in cities if x.name == "H"), None)
    cc.addAdjacent("J", 10)
    cc.addAdjacent("G", 10)
    cc.addAdjacent("E", 10)
    cc = next((x for x in cities if x.name == "I"), None)
    cc.addAdjacent("E", 10)
    cc.addAdjacent("F", 10)
    cc.addAdjacent("J", 20)
    cc = next((x for x in cities if x.name == "J"), None)
    cc.addAdjacent("G", 5)
    cc.addAdjacent("I", 20)


def generate(rndm, args):
    startIndex = city_names.index(start_city)
    individual = [0]*len(city_names) #individuo è un array di n elementi, ho 0 se non passo dalla citta, i altrimenti
    individual[startIndex] = 1
    newCity = start_city
    i = 1
    while newCity != end_city:
        city: City = next((x for x in cities if x.name == newCity), None)
        succIndex = random.randint(0,len(city.adjacentCities)-1)
        succCity = city.adjacentCities[succIndex][0]
        newCity = succCity
        cityIndex = city_names.index(succCity)
        if individual[cityIndex] == 0: #se non sono mai passato da questa città la aggiunge al path
            i += 1
            individual[cityIndex] = i
    return individual

def evaluate(individual, args):
    fitness = 10000
    if city_names[individual.index(1)] == start_city and city_names[individual.index(max(individual))] == end_city:
        try:
            i = 1
            cityIndex = individual.index(i)
            cityName = city_names[cityIndex]
            while cityName != end_city:
                city: City = next((x for x in cities if x.name == cityName), None)
                i+=1
                cityIndex = individual.index(i)
                cityName = city_names[cityIndex]
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


# ----------- INIZIO -----------------
CreateCitiesGraph()
inspyredWp = InspyredImpl(generate,evaluate) # genera una soluzione con il GA
genetic_sols = inspyredWp.getBestIndividuals(max_evaluations=100,
                                             num_elites=1,
                                             mutation_rate=0.1,
                                             pop_size=10)
bestIndividual = genetic_sols[0]
solAdapter = SolutionAdapter(city_names)
bestGASol = solAdapter.AdaptGASolution(bestIndividual)

#bestGASol = ["A","C","F","I","E","I","H","J"]
#bestGASol = ["A","B","D","G","H","J"]
print("SOLUZIONE ALGORITMO GENETICO: " + str(bestGASol))

dist = DistancePOI(bestGASol,levenshtein) # genera un oggetto DistancePoi prendendo in input la soluz. del GA ed una funzione

cp = SimpleCityProblem(start_city,end_city,dist, solAdapter) # costruisco il problema (fornisco in input le città e l'oggetto dist)
#cp = SimpleCityProblem(start_city,end_city,None, solAdapter) # costruisco il problema (fornisco in input le città e l'oggetto dist)
solution = astar(cp)
print("SOLUZIONE A*:" + str(solution))
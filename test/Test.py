import random

from CustomProblem.City import City
from CustomProblem.CityProblem import CityProblem
from heuristic_search.astar import astar
from test.DistancePOI import *
from test.LevenshteinDistance import *
from test.SolutionAdapter import SolutionAdapter

city_names = ["Arad", "Oradea", "Zerind", "Sibiu", "Timisoara", "Lugoj", "Mehadia",
              "Drobeta", "Craiova", "Rimnicu Vilcea", "Fagaras", "Bucarest", "Pitesti",
              "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Vaslui", "Iasi", "Neamt"]
cities = []
start_city = "Oradea"
end_city = "Eforie"

def CreateCitiesGraph():
    # creare le citta
    for c in city_names:
        ct = City(c)
        cities.append(ct)

    # crea il grafo
    cc = next((x for x in cities if x.name == "Arad"), None)
    cc.addAdjacent("Zerind", 75)
    cc.addAdjacent("Sibiu", 140)
    cc.addAdjacent("Timisoara", 118)

    cc = next((x for x in cities if x.name == "Timisoara"), None)
    cc.addAdjacent("Arad", 118)
    cc.addAdjacent("Lugoj", 140)

    cc = next((x for x in cities if x.name == "Lugoj"), None)
    cc.addAdjacent("Timisoara", 111)
    cc.addAdjacent("Mehadia", 70)

    cc = next((x for x in cities if x.name == "Mehadia"), None)
    cc.addAdjacent("Drobeta", 75)
    cc.addAdjacent("Lugoj", 70)

    cc = next((x for x in cities if x.name == "Zerind"), None)
    cc.addAdjacent("Arad", 75)
    cc.addAdjacent("Oradea", 71)

    cc = next((x for x in cities if x.name == "Oradea"), None)
    cc.addAdjacent("Sibiu", 151)
    cc.addAdjacent("Zerind", 71)

    cc = next((x for x in cities if x.name == "Sibiu"), None)
    cc.addAdjacent("Arad", 140)
    cc.addAdjacent("Oradea", 151)
    cc.addAdjacent("Fagaras", 99)
    cc.addAdjacent("Rimnicu Vilcea", 80)

    cc = next((x for x in cities if x.name == "Rimnicu Vilcea"), None)
    cc.addAdjacent("Pitesti", 97)
    cc.addAdjacent("Craiova", 146)
    cc.addAdjacent("Sibiu", 80)

    cc = next((x for x in cities if x.name == "Drobeta"), None)
    cc.addAdjacent("Mehadia", 75)
    cc.addAdjacent("Craiova", 120)

    cc = next((x for x in cities if x.name == "Craiova"), None)
    cc.addAdjacent("Pitesti", 138)
    cc.addAdjacent("Drobeta", 120)
    cc.addAdjacent("Rimnicu Vilcea", 146)

    cc = next((x for x in cities if x.name == "Fagaras"), None)
    cc.addAdjacent("Sibiu", 99)
    cc.addAdjacent("Bucarest", 211)

    cc = next((x for x in cities if x.name == "Bucarest"), None)
    cc.addAdjacent("Giurgiu", 90)
    cc.addAdjacent("Fagaras", 211)
    cc.addAdjacent("Pitesti", 101) #101
    cc.addAdjacent("Urziceni", 85)

    cc = next((x for x in cities if x.name == "Pitesti"), None)
    cc.addAdjacent("Rimnicu Vilcea", 97)
    cc.addAdjacent("Craiova", 138)
    cc.addAdjacent("Bucarest", 101) #101

    cc = next((x for x in cities if x.name == "Urziceni"), None)
    cc.addAdjacent("Hirsova", 98)
    cc.addAdjacent("Vaslui", 142)
    cc.addAdjacent("Bucarest", 85)

    cc = next((x for x in cities if x.name == "Hirsova"), None)
    cc.addAdjacent("Urziceni", 98)
    cc.addAdjacent("Eforie", 86)

    cc = next((x for x in cities if x.name == "Vaslui"), None)
    cc.addAdjacent("Urziceni", 142)
    cc.addAdjacent("Iasi", 92)

    cc = next((x for x in cities if x.name == "Iasi"), None)
    cc.addAdjacent("Neamt", 87)
    cc.addAdjacent("Vaslui", 92)

    cc = next((x for x in cities if x.name == "Neamt"), None)
    cc.addAdjacent("Iasi", 87)

    cc = next((x for x in cities if x.name == "Eforie"), None)
    cc.addAdjacent("Hirsova", 86)

    cc = next((x for x in cities if x.name == "Giurgiu"), None)
    cc.addAdjacent("Bucarest", 90)

# GENETIC FUNCTIONS


def gen(rndm,args):
    individual = [start_city]
    while individual[-1] != end_city:
        city:City = next((x for x in cities if x.name == individual[-1]), None)
        nextCityIndex = random.randint(0,len(city.adjacentCities)-1)
        (nextCity, cost) = city.adjacentCities[nextCityIndex]
        individual.append(nextCity)
    return individual


def eval(individual, args): #fitness function: negativo della somma delle distanze
    totalCost = 0
    if individual[0] != start_city or individual[-1] != end_city:
        totalCost = 10000
    else:
        for i in range(1,len(individual)):
            city:City = next((x for x in cities if x.name == individual[i]), None)
            prevCity = next((x for x in city.adjacentCities if x[0] == individual[i-1]), None)
            if prevCity is None:
                totalCost+=1000
            else:
                (c,cost) = prevCity
                totalCost += cost
    return -totalCost


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

# END GENETIC FUNCTIONS


# ----- MAIN START ----- #
CreateCitiesGraph()

#inspyredWp = InspyredImpl(generate,evaluate) # genera una soluzione con il GA
#genetic_sols = inspyredWp.getBestIndividuals(max_evaluations=50,
#                                             num_elites=1,
#                                             mutation_rate=0.1,
#                                             pop_size=10)
#bestIndividual = genetic_sols[0]
solAdapter = SolutionAdapter(city_names)
#bestGASol = solAdapter.AdaptGASolution(bestIndividual)
bestGASol = ["Oradea","Zerind","Arad","Sibiu","Fagaras","Bucarest","Urziceni","Hirsova","Eforie"]
print("SOLUZIONE ALGORITMO GENETICO: " + str(bestGASol))

dist = DistancePOI(bestGASol,levenshtein) # genera un oggetto DistancePoi prendendo in input la soluz. del GA ed una funzione

cp = CityProblem(start_city,end_city,dist, solAdapter) # costruisco il problema (fornisco in input le città e l'oggetto dist)
#cp = CityProblem(start_city,end_city,None, solAdapter) # costruisco il problema (fornisco in input le città e l'oggetto dist)
solution = astar(cp)
print("SOLUZIONE A*:" + str(solution))

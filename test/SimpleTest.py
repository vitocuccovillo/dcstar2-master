from CustomProblem.SimpleCityProblem import SimpleCityProblem
from heuristic_search.astar import astar
from test.DistancePOI import DistancePOI
from test.LevenshteinDistance import levenshtein
from test.SolutionAdapter import SolutionAdapter

city_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
start_city = "A"
end_city = "J"

# ----------- INIZIO -----------------

solAdapter = SolutionAdapter(city_names)
#bestGASol = ["A","C","F","I","E","I","H","J"]
bestGASol = ["A","B","D","G","H","J"]
print("SOLUZIONE ALGORITMO GENETICO: " + str(bestGASol))

dist = DistancePOI(bestGASol,levenshtein) # genera un oggetto DistancePoi prendendo in input la soluz. del GA ed una funzione

#cp = SimpleCityProblem(start_city,end_city,dist, solAdapter) # costruisco il problema (fornisco in input le città e l'oggetto dist)
cp = SimpleCityProblem(start_city,end_city,None, solAdapter) # costruisco il problema (fornisco in input le città e l'oggetto dist)
solution = astar(cp)
print("SOLUZIONE A*:" + str(solution))
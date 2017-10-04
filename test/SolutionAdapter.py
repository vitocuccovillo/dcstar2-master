#from test.Test import city_names


class SolutionAdapter(): #uniforma le soluzioni per renderle confrontabili

    def __init__(self, _args):
        self.args = _args


    #def AdaptGASolution(self, GASolution):
    #    return GASolution.candidate
    def AdaptGASolution(self, GASolution):
        solution = []
        for i in range(1,len(GASolution.candidate)):
            try:
                cityIndex = GASolution.candidate.index(i)
                if cityIndex != 0:
                    city = self.args[cityIndex]
                    solution.append(city)
            except:
                pass
        return solution


    def AdaptAStarSolution(self, AStarSolution):
        AStarSolutionFlat = []
        for (city, cost) in AStarSolution:
            AStarSolutionFlat.append(city)
        return AStarSolutionFlat
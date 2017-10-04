
class SolutionAdapter(): #uniforma le soluzioni per renderle confrontabili


    def AdaptGASolution(self, GASolution):
        return GASolution.candidate

    def AdaptAStarSolution(self, AStarSolution):
        AStarSolutionFlat = []
        for (city, cost) in AStarSolution:
            AStarSolutionFlat.append(city)
        return AStarSolutionFlat
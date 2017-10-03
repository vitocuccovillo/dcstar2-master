
class SolutionAdapter(): #uniforma le soluzioni per renderle confrontabili


    def AdaptGASolution(self, GASolution):
        GASolutionFlat = ""
        for c in GASolution.candidate:
            GASolutionFlat = GASolutionFlat + c
        return GASolutionFlat

    def AdaptAStarSolution(self, AStarSolution):
        AStarSolutionFlat = ""
        for (city, cost) in AStarSolution:
            AStarSolutionFlat = AStarSolutionFlat + city
        return AStarSolutionFlat
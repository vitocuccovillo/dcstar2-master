from heuristic_search.pqueue import PriorityQueue
from heuristic_search.node import Node
from test.Problem import Problem
from itertools import zip_longest
import operator


def astar(problem:Problem):
    numExpansions = 0
    closed = PriorityQueue()
    front = PriorityQueue()  # unlimited priority queue

    start_node = Node(problem.start_state)

    #estimated_node = (problem.estimate_cost(start_node.path()), start_node)
    #estim_cost = problem.g(start_node.path()) + problem.h(start_node.path()) #CALCOLO COSTO!
    estim_cost = GetCostTuple(problem.g(start_node.path()), problem.h(start_node.path()))
    estimated_node = (estim_cost, start_node)
    front.put(estimated_node)

    while not front.empty():
        (path_estimated_cost, current_node) = front.get()
        print("ESPANSIONE: " + str(current_node.state))
        numExpansions += 1
        current_state = current_node.state
        if not problem.unique_successors:
            closed.put((path_estimated_cost, current_node))
        if problem.goal(current_state):
            print("Numero espansioni A*: " + str(numExpansions))
            return current_node.path()  # solution found!
        else:
            successors = problem.successors(current_state)
            for successor_state in successors:
                # improve
                successor_node = Node(successor_state, parent_node=current_node)
                path_estimated_cost = GetCostTuple(problem.g(successor_node.path()), problem.h(successor_node.path()))
                #path_estimated_cost = problem.g(successor_node.path()) + problem.h(successor_node.path()) #CALCOLO COSTO!
                #path_estimated_cost = problem.estimate_cost(successor_node.path())
                if not problem.unique_successors:
                    estimated_node = front.find(successor_state)
                    if estimated_node is not None:
                        if path_estimated_cost < estimated_node[0]:
                            front.remove(estimated_node)
                            front.put((path_estimated_cost, successor_node))
                    else:
                        estimated_node = closed.find(successor_state)
                        if estimated_node is not None:
                            if path_estimated_cost < estimated_node[0]:
                                front.put((path_estimated_cost, successor_node))
                                closed.remove(estimated_node)
                        else:
                            front.put((path_estimated_cost, successor_node))
                else:
                    front.put((path_estimated_cost, successor_node))
    return None,numExpansions  # no solution found


# somma due tuple di lunghezza differente
def GetCostTuple(costs, heuristics):
    return [x + y for x, y in zip_longest(costs, heuristics, fillvalue=0)]
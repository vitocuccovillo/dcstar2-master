# Wrapper per librerie di algoritmi genetici

from abc import ABC, abstractmethod

class GeneticAbstractWrapper(ABC):

    @abstractmethod
    def eval_individual(individual, args):
        pass

    @abstractmethod
    def gen_individual(random, args):
        pass

    @abstractmethod
    def getBestIndividuals(max_evaluations, num_elites, mutation_rate, pop_size):
        pass
import random

import inspyred

from GAGuide.GeneticAbstractWrapper import GeneticAbstractWrapper


class InspyredImpl(GeneticAbstractWrapper):

    gen_function = None
    eval_function = None

    def __init__(self, _gen_function, _eval_function):
        InspyredImpl.gen_function = _gen_function
        InspyredImpl.eval_function = _eval_function

    @inspyred.ec.evaluators.evaluator
    def eval_individual(candidates, args):
        result = InspyredImpl.eval_function(candidates, args)
        return result

    def gen_individual(random, args):
        individual = InspyredImpl.gen_function(random,args)
        return individual

    def getBestIndividuals(self, max_evaluations, num_elites, mutation_rate, pop_size):
        rand = random.Random()
        rand.seed(10)
        ga = inspyred.ec.GA(rand)
        ga.observer = inspyred.ec.observers.stats_observer,
        ga.terminator = inspyred.ec.terminators.evaluation_termination,
        final_pop = ga.evolve(evaluator = InspyredImpl.eval_individual,
                              generator = InspyredImpl.gen_individual,
                              max_evaluations = max_evaluations,
                              num_elites = num_elites,
                              mutation_rate = mutation_rate,
                              pop_size = pop_size)
        final_pop.sort(reverse=True)
        return final_pop





from abc import ABC, abstractmethod, ABCMeta

class Problem(ABC):

    def __init__(self):
        raise NotImplementedError("You can't instantiate this class!")

    @abstractmethod
    def g(self, path):
        pass

    @abstractmethod
    def h(self, solutions_set):
        pass

    # @abstractmethod
    # def estimate_cost(self,path):
    #     pass

    @abstractmethod
    def goal(self, solutions_set):
        pass

    @abstractmethod
    def successors(self, solutions_set):
        pass

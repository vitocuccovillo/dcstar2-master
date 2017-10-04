from abc import ABC, abstractmethod, ABCMeta

class Problem(ABC):

    def __init__(self):
        raise NotImplementedError("You can't instantiate this class!")

    @abstractmethod
    def g(self, path):
        pass

    @abstractmethod
    def h(self, path):
        pass

    # @abstractmethod
    # def estimate_cost(self,path):
    #     pass

    @abstractmethod
    def goal(self, state):
        pass

    @abstractmethod
    def successors(self, state):
        pass

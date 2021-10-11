from abc import ABC
from abc import abstractmethod


class steps(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self,inputs):
        pass


class StepException(Exception):
    pass

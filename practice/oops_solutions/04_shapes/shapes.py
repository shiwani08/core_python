from abc import ABC, abstractmethod

class Shapes(ABC):

    @abstractmethod
    def calculate_area(self):
        pass
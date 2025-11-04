from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine():
        pass

    @abstractmethod
    def stop_engine():
        pass
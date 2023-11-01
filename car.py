from abc import ABC, abstractmethod
from battery import spindler_battery, nubbin_battery
from engine import capulet_engine, sternman_engine, willoughby_engine


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass

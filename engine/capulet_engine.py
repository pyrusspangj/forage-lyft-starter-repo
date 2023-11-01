from abc import ABC

from __init__ import Engine


class CapuletEngine(Engine, ABC):

    def __init__(self, current_mileage, last_service_mileage):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000

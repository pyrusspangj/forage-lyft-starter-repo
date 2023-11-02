from __init__ import Tire


class Octoprime(Tire):

    def __init__(self, worn):
        super().__init__()
        self.worn = worn

    def needs_service(self):
        return sum(self.worn) >= 3
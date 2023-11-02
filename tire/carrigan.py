from __init__ import Tire


class Carrigan(Tire):

    def __init__(self, worn):
        super().__init__()
        self.worn = worn

    def needs_service(self):
        return any(i >= 0.9 for i in self.worn)
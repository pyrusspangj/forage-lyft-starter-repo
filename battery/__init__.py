from abc import abstractmethod

class Battery:

    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
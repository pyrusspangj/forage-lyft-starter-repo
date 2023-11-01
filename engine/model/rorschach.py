from datetime import datetime

from ...car import Car

class Rorschach(Car):

    def __init__(self, battery, engine):
        super().__init__(engine, battery)
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        service_threshold_date = self.battery.last_service_date.replace(year=self.battery.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine.needs_service():
            return True
        else:
            return False
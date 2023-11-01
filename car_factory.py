from battery import spindler_battery, nubbin_battery
from engine import capulet_engine, sternman_engine, willoughby_engine
from engine.model import calliope, glissade, palindrome, rorschach, thovex


class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        return calliope.Calliope(battery, engine)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        return glissade.Glissade(battery, engine)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        engine = sternman_engine.SternmanEngine(warning_light_on)
        return palindrome.Palindrome(battery, engine)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        return rorschach.Rorschach(battery, engine)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        return thovex.Thovex(battery, engine)


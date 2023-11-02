import unittest
from datetime import datetime

from ..engine.model.calliope import Calliope
from ..engine.model.glissade import Glissade
from ..engine.model.palindrome import Palindrome
from ..engine.model.rorschach import Rorschach
from ..engine.model.thovex import Thovex
from ..battery.spindler_battery import SpindlerBattery
from ..battery.nubbin_battery import NubbinBattery
from ..engine.capulet_engine import CapuletEngine
from ..engine.willoughby_engine import WilloughbyEngine
from ..engine.sternman_engine import SternmanEngine

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        bat = SpindlerBattery(last_service_date, today)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Calliope(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        bat = SpindlerBattery(last_service_date, today)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Calliope(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        bat = SpindlerBattery(last_service_date, datetime.today())
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Calliope(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        bat = SpindlerBattery(last_service_date, datetime.today())
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Calliope(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        bat = SpindlerBattery(last_service_date, today)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Glissade(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        bat = SpindlerBattery(last_service_date, today)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Glissade(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        bat = SpindlerBattery(last_service_date, datetime.today())
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Glissade(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        bat = SpindlerBattery(last_service_date, datetime.today())
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Glissade(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        bat = SternmanEngine(warning_light_is_on)
        engine = SpindlerBattery(last_service_date, today)

        car = Palindrome(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False
        bat = SternmanEngine(warning_light_is_on)
        engine = SpindlerBattery(last_service_date, today)

        car = Palindrome(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        bat = SternmanEngine(warning_light_is_on)
        engine = SpindlerBattery(last_service_date, datetime.today())

        car = Palindrome(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        bat = SternmanEngine(warning_light_is_on)
        engine = SpindlerBattery(last_service_date, datetime.today())

        car = Palindrome(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        bat = NubbinBattery(last_service_date, today)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Rorschach(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        bat = NubbinBattery(last_service_date, today)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Rorschach(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        bat = NubbinBattery(last_service_date, datetime.today())
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Rorschach(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        bat = NubbinBattery(last_service_date, datetime.today())
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Rorschach(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        bat = NubbinBattery(last_service_date, today)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Thovex(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        bat = NubbinBattery(last_service_date, today)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Thovex(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        bat = NubbinBattery(last_service_date, datetime.today())
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Thovex(engine=engine, battery=bat)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        bat = NubbinBattery(last_service_date, datetime.today())
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Thovex(engine=engine, battery=bat)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()

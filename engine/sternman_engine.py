from abc import ABC

from __init__ import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on):
        super().__init__()
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self.warning_light_is_on

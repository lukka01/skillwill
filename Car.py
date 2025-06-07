from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, max_speed):
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value >= 0:
            self._max_speed = value
        else:
            print("Printed ")

    @property
    def current_speed(self):
        return self._current_speed

    # Setter for current_speed
    @current_speed.setter
    def current_speed(self, value):
        if 0 <= value <= self._max_speed:
            self._current_speed = value
        else:
            print(f"Speed must be between 0 and {self._max_speed}")

    def start_engine(self):
        return "Car started"

    def stop_engine(self):
        return "Car stopped"


class SportCar(Car):

    def start_engine(self):
        result = super().start_engine()
        print(result)
        print(f"Max_speed is - {self.max_speed}")

    def stop_engine(self):
        result = super().stop_engine()
        print(result)
        self.current_speed = 0


Opel = SportCar(max_speed=180)

Opel.start_engine()

Opel.current_speed = 120
Opel.stop_engine()

print(f"Current speed: {Opel.current_speed}")


class Person:
    def __init__(self, name:str, surname:str, heart_usage:int, brain_usage:int):
        self.name = name
        self.surname = surname
        self.heart = Heart(heart_usage)
        self.brain = Brain(brain_usage)

class Heart:
    def __init__(self, usage:int):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 70:
            print("high blood pressure")
        else:
            print("feeling Good")

class Brain:
    def __init__(self, usage:int):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 90:
            print("tired")
        else:
            print("rested")

class Leg:
    def __init__(self,person,moving_speed:int):
        self.person = person
        self.moving_speed = moving_speed

    @property
    def state(self):
        if self.moving_speed > 10:
            print("Running")
        elif self.moving_speed > 0:
            print("walking")
        else:
            print("Standing")





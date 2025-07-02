import abc

# ---- decorators ---- (not severeness)
def log_activity(func):
    """Decorator to log when an animal performs an action."""
    def wrapper(self, *args, **kwargs):
        # Access name directly from the instance or use get_name()
        animal_name = self.get_name() if hasattr(self, 'get_name') else self._name
        animal_class = self.__class__.__name__
        print(f"[{animal_name} the {animal_class}] is performing: {func.__name__.replace('_', ' ')}.")
        return func(self, *args, **kwargs)
    return wrapper

def hungry_check(func):
    """Decorator to ensure an animal is not too hungry before performing certain actions."""
    def wrapper(self, *args, **kwargs):
        if hasattr(self, '_hunger_level') and self._hunger_level > 70:
            animal_name = self.get_name() if hasattr(self, 'get_name') else self._name
            animal_class = self.__class__.__name__
            print(f"[{animal_name} the {animal_class}] is too hungry to perform {func.__name__.replace('_', ' ')}!")
            return
        return func(self, *args, **kwargs)
    return wrapper

# --- Mixins ---
class SwimmerMixin:
    """Mixin for animals that can swim."""
    @log_activity
    def swim(self):
        print(f"{self.get_name()} glides through the water.")

class FlyerMixin:
    """Mixin for animals that can fly."""
    @log_activity
    def fly(self):
        print(f"{self.get_name()} soars through the sky.")

class HunterMixin:
    """Mixin for animals that are predators."""
    @log_activity
    @hungry_check # This decorator relies on _hunger_level from Animal
    def hunt(self, prey):
        # Ensure prey also has a name to print
        prey_name = prey.get_name() if hasattr(prey, 'get_name') else "unknown prey"
        print(f"{self.get_name()} is attempting to hunt {prey_name}.")
        # Simulate hunting success/failure and hunger reduction
        if hasattr(self, '_hunger_level'):
            initial_hunger = self._hunger_level
            self._hunger_level = max(0, self._hunger_level - 50)
            if self._hunger_level < initial_hunger: # Simple check for successful hunt
                print(f"{self.get_name()} successfully hunted {prey_name}. Hunger level reduced to {self._hunger_level}.")
            else:
                print(f"{self.get_name()} failed to hunt {prey_name} (already too hungry or no change).")
        else:
            print(f"{self.get_name()} hunted {prey_name}.")


class Animal(abc.ABC):
    def __init__(self, name, species, age):
        self._name = name
        self._species = species
        self._age = age
        self._hunger_level = 50


    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_age(self):
        return self._age

    @property
    def hunger_level(self):
        """Property to access hunger level."""
        return self._hunger_level

    def get_hunger_level(self):
        return self._hunger_level

    @log_activity
    def eat(self, food_amount):
        """Reduces hunger level."""
        self._hunger_level = max(0, self._hunger_level - food_amount)
        print(f"{self.get_name()} ate {food_amount} units of food. Hunger level: {self._hunger_level}.")

    @log_activity
    def grow_older(self):
        """Increases age."""
        self._age += 1
        print(f"{self.get_name()} is now {self._age} years old.")

    @abc.abstractmethod
    @log_activity # Decorator applied to abstract method, will be inherited and used by implementations
    def make_sound(self):
        """Abstract method: All animals must make a sound."""
        pass

    @abc.abstractmethod
    @log_activity
    def move(self):
        pass

    def __str__(self):
        return f"{self._name} ({self._species}, {self._age} years old, Hunger: {self._hunger_level})"

# --- Inherited Classes ---

class Mammal(Animal):
    """Base class for mammals, inheriting from Animal."""
    def __init__(self, name, species, age, fur_color):
        super().__init__(name, species, age)
        self._fur_color = fur_color # Specific attribute for Mammals

    def get_fur_color(self):
        return self._fur_color

    @log_activity
    def move(self): # Implementation of abstract method (Polymorphism)
        print(f"{self.get_name()} walks on land.")

    @log_activity
    def make_sound(self): # Default sound for mammals (can be overridden)
        print("Generic mammal sound.")

class Bird(Animal):
    """Base class for birds, inheriting from Animal."""
    def __init__(self, name, species, age, wing_span):
        super().__init__(name, species, age)
        self._wing_span = wing_span # Specific attribute for Birds

    def get_wing_span(self):
        return self._wing_span

    @log_activity
    def move(self): # Implementation of abstract method (Polymorphism)
        print(f"{self.get_name()} hops on the ground.")

    @log_activity
    def make_sound(self): # Default sound for birds (can be overridden)
        print("Chirp!")

class Fish(Animal):
    """Base class for fish, inheriting from Animal."""
    def __init__(self, name, species, age, scale_type):
        super().__init__(name, species, age)
        self._scale_type = scale_type # Specific attribute for Fish

    def get_scale_type(self):
        return self._scale_type

    @log_activity
    def move(self): # Implementation of abstract method (Polymorphism)
        print(f"{self.get_name()} swims in the water.")

    @log_activity
    def make_sound(self): # Default sound for fish (can be overridden)
        print("Blub blub...")

# --- Concrete Animal Classes (Inheritance & Polymorphism & Mixins) ---

class Lion(Mammal, HunterMixin): # Inherits from Mammal, uses HunterMixin
    """A Lion, a type of Mammal and a Hunter."""
    def __init__(self, name, age, fur_color="golden"):
        super().__init__(name, "Lion", age, fur_color)

    @log_activity
    def make_sound(self): # Polymorphism: specific sound for Lion
        print("Roar!")

class Eagle(Bird, FlyerMixin, HunterMixin): # Inherits from Bird, uses FlyerMixin, HunterMixin
    """An Eagle, a type of Bird that can fly and hunt."""
    def __init__(self, name, age, wing_span):
        super().__init__(name, "Eagle", age, wing_span)

    @log_activity
    def make_sound(self): # Polymorphism: specific sound for Eagle
        print("Screech!")

class Shark(Fish, SwimmerMixin, HunterMixin): # Inherits from Fish, uses SwimmerMixin, HunterMixin
    """A Shark, a type of Fish that can swim and hunt."""
    def __init__(self, name, age, scale_type="placoid"):
        super().__init__(name, "Shark", age, scale_type)

    @log_activity
    def make_sound(self): # Polymorphism: specific sound for Shark
        print("Clicking and grinding sounds...")

class Penguin(Bird, SwimmerMixin): # Inherits from Bird, uses SwimmerMixin (but not FlyerMixin!)
    """A Penguin, a type of Bird that can swim but not fly."""
    def __init__(self, name, age, wing_span):
        super().__init__(name, "Penguin", age, wing_span)

    @log_activity
    def make_sound(self): # Polymorphism: specific sound for Penguin
        print("Squawk!")

    @log_activity
    def move(self): # Overridden move for specific Penguin movement (Polymorphism)
        print(f"{self.get_name()} waddles on land and dives into water.")

# --- Simulation ---
if __name__ == "__main__":
    print("--- Animal Kingdom Simulation ---")

    # Creating diverse animals
    lion = Lion("Leo", 5)
    eagle = Eagle("Aero", 3, "2 meters")
    shark = Shark("Jaws", 10)
    penguin = Penguin("Waddle", 2, "1 meter")
    zebra = Mammal("Zippy", "Zebra", 4, "black and white stripes")
    # A generic mammal
    dog = Mammal("Buddy", "Dog", 7, "brown")

    animals = [lion, eagle, shark, penguin, zebra, dog]

    print("\n--- Demonstrating Encapsulation & Basic Actions ---")
    print(lion) # Uses __str__ for easy printing of encapsulated data
    lion.eat(20)
    print(f"{lion.get_name()}'s current hunger level: {lion.get_hunger_level()}")
    lion.grow_older()
    print(f"{lion.get_name()} is now {lion.get_age()} years old.")
    print(f"Zebra's fur color: {zebra.get_fur_color()}")

    print("\n--- Demonstrating Abstraction & Polymorphism ---")
    for animal in animals:
        print(f"\n--- {animal.get_name()} the {animal.get_species()} ---")
        animal.make_sound() # Polymorphism in action
        animal.move()       # Polymorphism in action

    print("\n--- Demonstrating Mixins and Decorators ---")
    # Lion hunting (HunterMixin)
    print("\n--- Leo the Lion actions ---")
    lion.hunt(zebra)
    lion.eat(30) # make sure lion is not too hungry for the next hunt
    lion.hunt(dog) # try hunting another animal

    # Eagle flying and hunting (FlyerMixin, HunterMixin)
    print("\n--- Aero the Eagle actions ---")
    eagle.fly()
    eagle.hunt(penguin) # Eagle trying to hunt a penguin (conceptual)

    # Shark swimming and hunting (SwimmerMixin, HunterMixin)
    print("\n--- Jaws the Shark actions ---")
    shark.swim()
    shark.hunt(lion) # Shark trying to hunt a lion (conceptual)

    # Penguin swimming (SwimmerMixin)
    print("\n--- Waddle the Penguin actions ---")
    penguin.swim()
    penguin.move() # Penguin's overridden move method
    penguin.make_sound()

    print("\n--- Testing hungry_check decorator ---")
    hungry_lion = Lion("Grumpy", 6)
    # Make Grumpy very hungry
    hungry_lion.eat(10)
    print(f"Grumpy's initial hunger level: {hungry_lion.get_hunger_level()}")
    hungry_lion.hunt(zebra) # This should trigger the hungry_check decorator as hunger > 70
    hungry_lion.eat(100) # Feed the lion generously
    print(f"Grumpy's hunger level after eating: {hungry_lion.get_hunger_level()}")
    hungry_lion.hunt(zebra) # Now it should be able to hunt

    print("\n--- End of Animal Kingdom Simulation ---")


# python garbage_collector
# python __del__
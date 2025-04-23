-- Assignment 1 --
# Name: Denis Omwoyo

# Base Class
class Superhero:
    def __init__(self, name, alias, superpower, strength_level):
        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.strength_level = strength_level

    def introduce(self):
        return f"I am {self.alias}, known as {self.name}, and I have the power of {self.superpower}!"

    def power_boost(self, boost_amount):
        self.strength_level += boost_amount
        return f"{self.alias}'s strength level increased to {self.strength_level}!"

    def get_status(self):
        return {
            "Name": self.name,
            "Alias": self.alias,
            "Superpower": self.superpower,
            "Strength Level": self.strength_level
        }


# Subclass with Polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, alias, superpower, strength_level, flight_speed):
        super().__init__(name, alias, superpower, strength_level)
        self.flight_speed = flight_speed  # New attribute for FlyingHero

    def fly(self):
        return f"{self.alias} takes off into the sky at {self.flight_speed} km/h!"

    # Polymorphic method
    def introduce(self):
        return f"I soar through the skies! I'm {self.alias}, the flying hero with {self.superpower}."


# Another Subclass
class TechHero(Superhero):
    def __init__(self, name, alias, superpower, strength_level, gadget):
        super().__init__(name, alias, superpower, strength_level)
        self.gadget = gadget

    def use_gadget(self):
        return f"{self.alias} uses their gadget: {self.gadget}!"

    def introduce(self):
        return f"I'm {self.alias}, and my tech-powered skill is {self.superpower}!"

# Testing the classes
hero1 = FlyingHero("Clark Kent", "Superman", "Flight & Strength", 95, 1200)
hero2 = TechHero("Tony Stark", "Iron Man", "Advanced Armor", 88, "Arc Reactor")

print(hero1.introduce())
print(hero1.fly())
print(hero1.power_boost(5))

print(hero2.introduce())
print(hero2.use_gadget())
print(hero2.get_status())

-- Activity 2 --

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses should implement this method.")

# Subclasses with different move() implementations
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on water 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling on the street 🚲"

# A function that uses polymorphism
def start_journey(vehicle: Vehicle):
    print(vehicle.move())

# Testing different vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    start_journey(v)

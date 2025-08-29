Base class
class Vehicle:
    def init(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        pass  # To be overridden by subclasses

Inheritance and polymorphism
class Car(Vehicle):
    def move(self):
        return "Driving "

class Plane(Vehicle):
    def move(self):
        return "Flying "

Usage
car = Car("Toyota", "Corolla")
plane = Plane("Boeing", "747")

print(f"{car.brand} {car.model}: {car.move()}")
print(f"{plane.brand} {plane.model}: {plane.move()}")

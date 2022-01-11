"""
Inheritance:

Class A ---> Base class / Parent class
    def add(self):

Class B ---> Derived class / Child class        # Single level Inheritance
    def add(self):

so from Inheritance we can access members, properties and functions from another class

Class A <--- Class B <--- Class C   # Multilevel Inheritance
"""
class VehiclePrice():
    price = 100

class Car(VehiclePrice):            # For Multilevel Inheritance example
    transmission = 'CVT'
    def carStart(self):
        print("Car can start")

class BMW(Car):
    fuelType = "Electric Vehicle"
    def theftSafety(self):
        print("Theft safety mechanism by BMW")

bmw = BMW()
bmw.carStart()
bmw.theftSafety()
print("Transmission of BMW is: ", bmw.transmission)
print("My BMW car is an {}".format(bmw.fuelType))
print("My BMW price is: Rs.", bmw.price)        # Multilevel inheritance example
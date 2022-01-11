"""
Inheritance:

Class A ---> Base class / Parent class
    def add(self):

Class B ---> Derived class / Child class        # Single level Inheritance
    def add(self):

so from Inheritance we can access members, properties and functions from another class
"""
class Car():
    transmission = 'DCT'
    def carStart(self):
        print("Car can start")

class BMW(Car):
    fuelType = "Electric Vehicle"
    def theftSafety(self):
        print("Theft safety mechanism of BMW Car")

bmw = BMW()
bmw.carStart()
bmw.theftSafety()
print("Transmission of BMW is: ", bmw.transmission)
print("My BMW car is an {}".format(bmw.fuelType))

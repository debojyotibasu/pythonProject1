"""
Inheritance:

Class A ---> Base class / Parent class
    def add(self):

Class B ---> Derived class / Child class        # Single level Inheritance
    def add(self):

so from Inheritance we can access members, properties and functions from another class

Class A <--- Class B <--- Class C   # Multilevel Inheritance

Class A         Class B
        Class C                     # Multiple Inheritance

"""
class VehiclePrice():
    price = 100
    def driveType(self):
        print("4 Wheel Drive - from VehiclePrice class")

class Car():                        # For Multiple Inheritance example
    transmission = 'CVT'
    def carStart(self):
        print("Car can start")
    def driveType(self):
        print("4 Wheel Drive - from Car class")

class Audi(VehiclePrice, Car):       # Multiple inheritance example
    fuelType = "Electric Vehicle"
    def theftSafety(self):
        print("Theft safety mechanism by Audi")

audi = Audi()
audi.carStart()
audi.theftSafety()
print("Transmission of Audi is: ", audi.transmission)
print("My Audi car is an {}".format(audi.fuelType))
print("My Audi price is: Rs.", audi.price)        # Multiple inheritance example
audi.driveType()


class Car:
    wheels = 4                          # Class level variable - Static

    def __init__(self):
        self.model = "Maruti"           # Instance Variable - Changable
        self.colour = "Red"             # Instance Variable - Changable

    def getCarModel(self):              # Instance Method which uses Instance variables of the class
        print(self.model)

    @classmethod                        # Known as decorator
    def getWheelsCount(cls):            # Class level Method which uses class level variables of the class
        print(cls.wheels)

    @staticmethod                       # Known as decorator
    def VehicleWarningMessage():        # Static method for general purpose
        print("Obey traffic rules")


c1 = Car()
c2 = Car()
c3 = Car()
c3.model = "Tata"
c3.colour = "Black"
# c3.wheels = 5
Car.wheels = 20
print(c1.model, c1.colour, c1.wheels)
c1.getCarModel()
c1.getWheelsCount()
print(c2.model, c2.colour, c2.wheels)
Car.VehicleWarningMessage()
print(c3.model, c3.colour, c3.wheels)
Car.getWheelsCount()

'''
3 types of methods/functions
1. Instance Method  - Use to access instance variable of the class
2. Class Method - Use to access class level variable of the class
3. Static Method - Standalone method
'''
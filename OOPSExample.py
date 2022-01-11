"""
OOPS Concepts/Procedural Language (Step By Step implementation of the code)
1. Classes
2. Objects
3. Encapsulation
4. Abstraction
5. Inheritance
6. Polymorphism
"""

"""
Question: What is a Class?
Answer: A Class can be defined as a Blueprint / Template which describes the state / behaviour of it's object.
Synrax:
class <classname>:
    statements
"""

class Car1:
    car_price = 9999
    car_model = "sports"

    def start_function(self):
        print("Car can start")

    def stop_function(self):
        print("Car can stop")

    def accelerate_funtion(self):
        print("Car can accelarate")

c1 = Car1()

c1.start_function()
c1.stop_function()
c1.accelerate_funtion()

class Car2:
    car_price = None
    car_transmission = "CVT"

    def start_function(self, model):
        print("Start the {} car".format(model))

    def transmission_function(self, car_transmission):
        print("You have chosen {} transmission of the car".format(car_transmission))

    def bookingPrice_funtion(self, car_price):
        print("On Road Price of your car should be: {}".format(car_price))

    def booking_funtion(self):
        print("Congratulation, you have successfully booked your car")


c2 = Car2()

c2.start_function("Tata")
c2.transmission_function("AMT")
c2.bookingPrice_funtion(500000)
c2.booking_funtion()
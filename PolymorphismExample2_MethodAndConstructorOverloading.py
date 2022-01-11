'''
Polymorphism:
    1. Operator overloading
    2. Method overloading / overriding
    3. Constructor overloading / overriding
'''

'''
#  2. Method and Constructor overloading / overriding

Method Overriding
class A:
    def add():
        print("Addition of X and Y")

class B(A):
    def add():
        print("Different Definition")
    
'''

# Method and Constructor Overloading - Not supported by Python
class MethodOverloading:

    def __init__(self):
        print("Inside default constructor")

    def __init__(self, name):
        self.name = "Debojyoti"
        print("Inside parameterized constructor")

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

obj3 = MethodOverloading("Aritra")
#print(obj3.add(10, 20))
print(obj3.add(10, 20, 30))
obj4 = MethodOverloading("Saikat")
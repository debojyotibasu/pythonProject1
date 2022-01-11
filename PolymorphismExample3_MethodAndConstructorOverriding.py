'''
Polymorphism:
    1. Operator overloading
    2. Method overloading / overriding
    3. Constructor overloading / overriding
'''

# Method and Constructor Overriding
class MethodOverridingBase():
    def __init__(self):
        print("Inside Base Class Constructor")

    def a(self):
        print("Inside Base Class")

class MethodOverridingDerived(MethodOverridingBase):
    def __init__(self):
        super().__init__()
        print("Inside Derived Class Constructor")

    '''
        def a(self):
        print("Inside Derived Class")
    '''
    def b(self):
        print("Some other function")

    def a(self):
        super().a()
        print("Inside Derived Class")

obj5 = MethodOverridingDerived()
obj5.a()
'''
Polymorphism:
    1. Operator overloading
    2. Method overloading / overriding
    3. Constructor overloading / overriding
'''


#  2. Method and Constructor overloading / overriding
class OperatorOverloading:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        # total_pages = self.pages + other.pages
        total_pages = self.pages - other.pages
        return total_pages


obj1 = OperatorOverloading(10)
obj2 = OperatorOverloading(5)
print(obj1 + obj2)

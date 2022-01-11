"""
Constructors:
They are called as a first function of the class.

Syntax:
__init__()

All classes have this function which is always executed when the class is being initiated or an Object of the class
is created

Point to remember: Constructor overloading is not possible in Python like Java
"""

class Calculator:
    def __init__(self):
        print("Inside Constructor")

    def addition(self):
        print("Adding some numbers")

calc1 = Calculator()
calc1.addition()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showEmp(self):
        print("Name of employee: ", self.name)
        print("ID of employee: ", self.id)

emp1 = Employee("Mrinmoy", 'CG9342')
emp1.showEmp()
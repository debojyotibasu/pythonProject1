'''
3 types of Access Specifier
1. Public
2. Private: Members should start with a single underscore, _var, def _method(). Protected members should be
accessed from the same class, or from the derived classes.
3. Protected: Members should start with a double underscore, __var, def __method(). Private members should be
accessed from the same class only.
'''

class Car:
    publicVar = 9
    _protectedVar = 10
    __privateVar = 11

    def __init__(self):
        print("Inside Car Constructor")

    def publicMethod(self):
        print("Calling Public Method")

    def _protectedMethod(self):
        print("Calling Protected Method")

    def __privateMethod(self):
        print("Calling Private Method")
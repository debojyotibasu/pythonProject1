'''
3 types of Access Specifier
1. Public - Same Class, Derived Class, Other Class
2. Protected - _var, def _RajatFunction(). Same Class, Derived Class
3. Private - __var, def __RajatFunction(). Same Class
'''

class Car:
    publicVar = 9
    _protectedVar = 10
    __privateVar = 11

    def __init__(self):
        print("Inside Car constructor")

    def publicMethod(self):
        print("Calling Public Method")

    def _protedtedMethod(self):
        print("Calling Protected Method")

    def __privateMethod(self):
        print("Calling Private Method")
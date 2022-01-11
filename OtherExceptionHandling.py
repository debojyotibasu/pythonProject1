'''
1. Exception
2. Error

try:
    "----------------"
except:
    "----------------"
'''

try:
    a = int(input("Enter the value for first number: "))
    b = int(input("Enter the value for second number: "))
    c = a / b
    print("Result is {}".format(c))

    print("End of program")
except (ZeroDivisionError, ValueError):
    print("Please enter a valid number")
else:
    print("Inside Else block - Only execute if Try block has no exception")
finally:
    print("I am in Finally block")

print("Outside Try-Except block")

'''
Python Exception Hierarchy

BASE EXCEPTION
    1. Exception
        a. Attribute Exception/Error
        b. Arithmatic Exception/Error
            i. ZeroDivision Error
            ii. FloatingPoint Error
            iii. Overflow Error
        c. EOF Exception (End of File)
        d. Name Exception
    2. System Exit
    3. Generator Exit
    4. Keyboard Interrupt
'''

# print(a1)


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
except:
    print("Please enter a valid number")
else:
    print("Inside Else block - Only execute if Try block has no exception")

print("Outside Try-Except block")
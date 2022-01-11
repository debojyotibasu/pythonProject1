"""
Python Operators:
1. Arithmetic
2. Comparison
3. Equality
4. Logical
5. Bitwise
6. Shift
7. Assignment
8. Ternary
9. Membership
10. Identity
"""

"""
Arithmetic Operators
1. Addition         ( + )
2. Subtraction      ( - )
3. Multiplication   ( * )
4. Division         ( / )
5. Modulus          ( % )
6. Exponential      ( ** )
7. Floor Division   ( // )
"""

a = 22
b = 3
print("Arithmetic Operators")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
print("=====================")

"""
Comparison Operators (Also known as Relational Operators)
1. Greater than             ( > )
2. Greater than or Equal    ( >= )
3. Less than                ( < )
4. Greater than or Equal    ( <= )
"""
c = 10
d = 52
print("Comparison Operators")
print(c > d)
print(c >= d)
print(c < d)
print(c <= d)
print("------------------")

e = "Cat"       # ASCII value of C is 67
f = "Dog"       # ASCII value of C is 68
print(e > f)
print(e >= f)
print(e < f)
print(e <= f)
print("=====================")

print("Example of Relational Operator Chaining")
print(10 < 20 < 30 < 40)
print("=====================")

"""
Equality Operators
1. Equal to     ( == )
2. Not Equal to ( != )
"""
print("Equality Operators")
g = 10
h = 20
print(g == h)
print(g != h)
print("------------------")
print(1 == True)
print(0 == True)
print(0 == False)
print(10 == 10.0)
print("Debojyoti" == "Debojyoti")
print("=====================")

"""
Logical Operators
1. And  (Returns true whenever both the arguments are true in nature)
2. Or   (Returns true whenever if any one of the arguments is true in nature)
3. Not  (Always returns the reverse complement)

Condition1: If the value x (first value), evaluates to False then the result is the value of x
Condition2: If the value x (first value, evaluates to True then the result is the value of y
"""
print(True and True)
print(1 and 0)
print(0 and 20)
print(10 and 20)

print(10 or 20)
print(0 or 20)

# username1 = input("Enter Username: ")
# password1 = input("Enter Password: ")
# if username1 == "Debojyoti" and password1 == "123":
#     print("Valid User")
# else:
#     print("Invalid User")
#
# username2 = input("Enter Username: ")
# password2 = input("Enter Password: ")
# if username2 == "Debojyoti" or password2 == "123":
#     print("Valid User")
# else:
#     print("Invalid User")

print(not True)
print(not False)

a = 10
b = 20
print(not a == 10)
print(not b == 10)
print("=====================")

"""
Bitwise Operators
1. Bitwise And          ( & )   If both the bits are same, then the result should be 1 otherwise it will always be 0
2. Bitwise Or           ( | )   If atleast any one bit is 1, then the result is 1 otherwise it is 0
3. Bitwise XOR          ( ^ )   If both bits are different, then the result is 1 otherwise it is 0
4. Bitwise Complement   ( ~ )   
"""


print(bin(16))
print(bin(18))
print("-----------Bitwise &-----------")
print(16 & 18)
print("-----------Bitwise |-----------")
print(16 | 18)
print("-----------Bitwise XOR-----------")
print(16 ^ 18)
print("Decimal number of binary 0b00010 is", 0b00010)
print("-----------Bitwise Complement or One's complement operator-----------")
print(~(-10))
print(~(10))
print("=====================")

"""
Shift Operators
1. Left Shift       ( << )
2. Right Shift      ( >> )
"""
print(bin(10))
print(0b101000)
print(10 << 2)
print(0b10)
print(10 >> 2)

"""
Assignment Operators    ( = , += , -= , *= etc. )
"""
print("-----------Assignment Operators-----------")
x = 10
print(x)
x += 10
print(x)
x *= 10
print(x)
x -= 10
print(x)
x /= 10
print(x)

# Increment and Decrement operators are supported by Python

"""
Ternary Operators
It is a Conditional Operator
But there is no specific keyword for ternary operator
Example:
    Var = First value if condition Else second value
"""
a = 50
b = 20
c = 30 if a > b else 40
print(c)

# m = int(input("Enter first value: "))
# n = int(input("Enter second value: "))
# min = m if m < n else n
# print(min)


"""
Identity Operators
    is
    is not
    
    a is not b, return true only when two reference var are pointing to the same object
"""
p = 10
q = 10
print(p is q)
print(p is not q)

"""
Membership Operators
    in
    not in
"""
u = [10, 20, 30, 50, "xyz"]
print(30 in u)
print("wxyz" in u)
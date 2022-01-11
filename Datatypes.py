# Numeric Datatype
import math

x = 10
y = 20.3
z = 5j
print(type(x))
print(isinstance(x,int))
print(type(y))
print(isinstance(y,int))
print(type(z))
print(isinstance(z,complex))

# String
a = "Debojyoti"
print(type(a))
print(isinstance(a,str))

# Boolean
b = True
print(type(b))
print(isinstance(b,bool))

# List
c = ["One", "Two", "Three"]
print(type(c))
print(isinstance(c, list))

# Tuple
d = ("One", "Two", "Three")
print(type(d))
print(isinstance(d, list))

# Set
e = {"One", "Two", "Three"}
print(type(e))
print(isinstance(e, set))

# Frozen Set
f = frozenset({"One", "Two", "Three"})
print(type(f))
print(isinstance(f, set))

# Dictionary
g = {"firstName":"Debojyoti", "lastName":"Basu"}
print(type(g))
print(isinstance(f, dict))

# Some numeric operation
print(3 + 6)    # 3 PLUS 6
print(3 * 6)    # 3 INTO 6
print(3 ** 6)   # 3 To THE POWER 6

h = -802308329123456789
print(type(h))

'''
Generate Random Numbers from 18 to 65
'''
import random
print(random.randrange(18,65))

print("Numeric result:" , 10 - 5)       #Ans: Numeric result: 5
print("Numeric result:" , 10 * 5)       #Ans: Numeric result: 50
print("Boolean result:" , 10 > 5)       #Ans: Boolean result: True
print("Boolean result:" , 10 < 5)       #Ans: Boolean result: False
print("Boolean result:" , 10 == 5)      #Ans: Boolean result: False

# Some floating operation
import math
print(math.pi)
print(type(math.pi))

j = 1.1111111111111118
print(j)        # Rounds the 16th digit

print(10 / 5)   # Always shows the value in decimal
print(10 // 5)  # If you do not want to accept decimal value
print(21 // 4)  # You will loose the remaning part
print(21 % 4)   # Remainder part you will get by using modulus
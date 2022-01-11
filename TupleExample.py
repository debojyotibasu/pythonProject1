"""
Tuples:
1. It is used to store the sequence of IMMUTABLE objects
2. Mostly all other operations are similar to a list

Question:
If List and Tuples are same then what is the benefit to use tuple
Answer:
For "Static" variable/function we use tuple so that value not change like List. e.g. DOB, University Name etc.
"""

T1 = ("Debojyoti", 2.76, 93, True)
print(type(T1))

"""
T1[2] = 20
print(T1)       // TypeError: 'tuple' object does not support item assignment
"""

"""
Tuple slicing/indexing
"""
T2 = (0, 1, 2, 3, 4, 5)
print(T2[:])        # (0, 1, 2, 3, 4, 5)
print(T2[0:])       # (0, 1, 2, 3, 4, 5)
print(T2[1:2])      # (1,)
print(T2[2:4])      # (2, 3)
print(T2[:4])       # (0, 1, 2, 3)

"""
Delete item from Tuple not possible
"""
# del T2[3]           # TypeError: 'tuple' object doesn't support item deletion
# print(T2)

"""
Tuple Operations:
1. Repetation
2. Concatenation
3. Membership Operation
4. Iteration
"""
T3 = ("Laurel", 2.3)
print(T3 * 2)                   # Repetation

T4 = ("Hardy", True)
print(T3 + T4)                  # Concatenation

print("Laurel" in T3)           # Membership OPeration
print("Hardy" not in T4)        # Membership OPeration

for T5 in ("Vaishali", 987.65, True, 4):
    print(T5)                   # Iteration
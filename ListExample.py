"""
Other Datatypes:
1. List
2. Dictionary
3. Tuples
"""

"""
List:
1. It is just a consecutive collection of related items/words
2. Represents a group of values as a single entity, order is very important
3. It allows duplicate values as well
4. It is represented by a square brackets
5. Values are separated by commas
6. List is mutable in nature, can append values
"""
a = []  # Empty list
b = [1, 2.3, "Debojyoti", True, 2.3]  # Index starts from 0, can hold duplicate values
print(type(b))
print(b)
print(b[2])  # Where order is preserved
print(b[4])
# print(b[5])    # IndexError: list index out of range
b.append("Basu")
print(b[5])

Player = ['Ronaldo', 'Messi', 'Mohamed Salah']
Team = ['Liverpool F.C.', 'Manchester United F.C.', 'Paris Saint-Germain F.C.']
Age = [29, 34, 36]
print(f"Player name is {Player[0]}, Age is {Age[2]} and Current Team is {Team[1]}")
print(f"Player name is {Player[1]}, Age is {Age[1]} and Current Team is {Team[2]}")
print(f"Player name is {Player[2]}, Age is {Age[0]} and Current Team is {Team[0]}")

"""
List Slicing
"""
print("============= List Slicing =============")
c = [0, 1, 2, 3, 4, 5, 6]
print(c[0:])        # [0, 1, 2, 3, 4, 5, 6]
print(c[:])         # [0, 1, 2, 3, 4, 5, 6]
print(c[2:4])       # [2, 3]
print(c[:4])        # [0, 1, 2, 3]

"""
Updating List Values
"""
print("============= Updating List Values =============")
d = [1, 2, 3, 4, 5, 7]
print(d)
d[5] = 6
print(d[:])
d[1:4] = ['Debojyoti', True, 22]
print(d)
d[1:4] = ['Basu', 41]
print(d)

"""
Delete List Values
"""
print("============= Delete List Values =============")
del d[3]
print(d)

"""
Sorting List Values
"""
print("============= Sorting List Values =============")
e = ['a', 'e', 'd', 'b', 'c']
print(e)
e.sort()
print(e)
e.sort(reverse=True)
print(e)


"""
List Operations
1. Repetition Operation
2. Concatenation Operation
3. Membership Operation
4. Iteration
5. Lenght Function
"""

"""
1. Repetition Operation
"""
print("============= Repetition Operation =============")
f = [1, 2.3, "Debojyoti", True]
f = f * 2
print(f)

"""
2. Concatenation Operation
"""
print("============= Concatenation Operation =============")
g = [5, 9.43, "Basu", False]
print(f + g)

"""
3. Membership Operation
"""
print("============= Membership Operation =============")
print("Basu" in f)
print("Debojyoti" in g)

"""
4. Iteration
"""
print("============= Iteration =============")
for i in g:
    print(i)

"""
5. Lenght Function
"""
print("============= Lenght Function =============")
print(len(f))

"""
Some Other Functions
"""
print("============= Some Other Functions =============")
j = [11, 32, 79, 92.31, 44,1, 49, 88, 37, 56, 92]
k = "Vijay"
print("Highest value of j is: ", max(j))
print("Lowest value of j is: ", min(j))
l = list(k)
print(l)
print(type(k))
print(type(l))
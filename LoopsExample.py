"""
Loops are iterative statments:
1. For Loop
2. While Loop
"""

"""
1. For Loop:
    For every x, in the sequence to perform the activity, which means every statement which is available in the
    sequence, range, list, tuple or a dictionary
    
    Example: for x in sequence
                statements
"""

sequence = "Basu"
for y in sequence:
    print(y)

sequence = "Debojyoti"
a = 0
for x in sequence:
    print("The character present at {} index is {}".format(a, x))
    a = a + 1

for y in range(5):
    print("Hello World!!!", y)

for z in range(1, 6):
    print("Welcome Students", z)

for i in range(3, 33, 3):
    print(i)

j = int(input("Which table you want to print? "))
for k in range(1, 11):
    print(j, " * ", k, " = ", j * k)


List = eval(input("Enter numbers for addition: "))

sum = 0
for p in List:
    sum = sum + p
print("The sum is: ", sum)

str = "I am Debojyoti"
s = str.split(" ")
for q in s:
    print(q)


# For practice Python use "https://codingbat.com/python"

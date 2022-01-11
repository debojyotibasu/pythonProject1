"""
Break: it is used to Break the current loop and resume the other code
"""
for i in range(10):
    if i == 7:
        print("Executing break at ", i)
        break
    print("Printing the value of i = ", i)
print("Outside the for loop")

"""
Continue: it is used to skip the current iteration and continue with the next iteration
"""
print("============= Print Odd Numbers =============")
for i in range(1, 11):
    if i % 2 == 0:
        continue
        print("Even number is: ", i)
    print("Odd number is: ", i)

print("============= Another Continue Example =============")
for i in range(10):
    if i == 7:
        print("Executing break at ", i)
        break
    elif i == 5:
        continue
    print("Printing the value of i = ", i)
print("Outside the for loop")

"""
Else block within the loop: it is used to skip the current iteration and continue with the next iteration
"""
print("============= Example1: Else block within the loop =============")
cart = [10, 20, 600, 30, 40, 50, 550]
for item in cart:
    if item > 500:
        print("This item is not allowed")
        break
    print(item)
else:
    print("All items are successfully processed")

print("============= Example2: Else block within the loop =============")
cart = [10, 20, 600, 30, 40, 50, 550]
for item in cart:
    if item > 500:
        print("This item is not allowed")
        continue
    print(item)
else:
    print("All items are successfully processed")

print("============= Pass Statement =============")
for x in "Debojyoti":
    pass

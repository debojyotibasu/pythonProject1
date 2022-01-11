"""
While condition/true
    execute the block
"""
a = 1
while a <= 10:
    print("Hello")
    a += 1
print("==============================")

num = int(input("Enter the number: "))
sum = 0
count = 1

while count <= num:
    sum = sum + count
    count += 1
print("Sum of {} numbers is :{}".format(num, sum))
print("==============================")
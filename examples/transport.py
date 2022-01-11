from AccessSpecifiersExample import Car

car = Car()
print(car.publicVar)
print(car._protectedVar)
# print(car.__privateVar)
print(car._Car__privateVar)

car.publicMethod()
car._protectedMethod()
#car.__privateMethod()
car._Car__privateMethod()
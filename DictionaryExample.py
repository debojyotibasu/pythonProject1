"""
Other Datatypes:
1. List
2. Dictionary
3. Tuples
"""

"""
Dictionary: Key and Value pair
1. Key - Numbers, String, Tuples
2. Value - Python Object
"""
D1 = {
    "Name" : "Udayan",
    "Age" : 26,
    "Salary": 10000.76,
    "Organisation" : "ABC Co. Pvt. Ltd.",
    "Is_Married" : False
}
print(type(D1))
print(D1)
print("Name: {}".format(D1["Name"]))
print("Age: {}".format(D1["Age"]))
print("Salary: {}".format(D1["Salary"]))
print("Organisation: {}".format(D1["Organisation"]))
print("Is_Married: {}".format(D1["Is_Married"]))

"""
Update Dictionary
"""
print("============= Update Dictionary =============")
"""
D1["Name"] = input("Enter your name: ")
D1["Age"] = int(input("Enter your age: "))
D1["Salary"] = float(input("Enter your salary: "))
D1["Organisation"] = input("Enter your organisation name: ")
D1["Is_Married"] = bool(input("Are you married: "))
print(D1)
"""

"""
Update Dictionary Item
"""
del D1["Is_Married"]
print(D1)

"""
Iterate Dictionary
"""
print("============= Iterate Dictionary keys =============")
for keys in D1:
    print(keys)

print("============= Iterate Dictionary Values =============")
for values in D1:
    print(D1[values])

print("============= Iterate Dictionary Values Other Method =============")
for values in D1.values():
    print(values)

print("============= Print Dictionary Keys and Values in couple =============")
for keyValues in D1.items():
    print(keyValues)

print("============= Dictionary in the form of List =============")
bazaar1 = {
    "Fruits" : ["Apple", "Banana", "Cucumber"],
    "Price" : 120,
    "Quantity" : 1.5
}
print(bazaar1)
print(bazaar1["Fruits"])
print(bazaar1["Fruits"][0])

print("============= Dictionary within Dictionary =============")
bazaar2 = {
    "Location" : "India",
    "Fruits" : {"Name" : "Grapes", "Price" : 160}
}
print(type(bazaar2))
print(bazaar2)
print(bazaar2["Fruits"])
print(bazaar2["Fruits"]["Name"])
print(bazaar2.get("Fruits").get("Price"))
print("Length of dictionary bazaar2 is: ", len(bazaar2))
print("All keys of bazaar2 dictionary: ", bazaar2.keys())

"""
Set:
1. It is similar to a list
2. It can store different type of values (Objects) String, Int, Float, Bool etc.
3. Set cannot have duplicate values
4. Set are defined {}
5. It is a collection which is unordered and unindexed

Question:
Difference between Set and List
Answer:
1. Unlike List, Set cannot accept duplicate values
2. "Repetition Operation" and "Concatenation Operation" are not allowed in Set
"""
S1 = {"Debojyoti", False, 123.45, 67, "Selenium", "Debojyoti", True, 67, "Selenium"}
print(type(S1))     # <class 'set'>
print(S1)           # Unordered values can be seen, Unindexed also
print(len(S1))      # 6

print("================= Print all values of set =================")
for i in S1:
    print(i)

print("================= Add element to existing set =================")
S1.add("Rest_Assured")
print(len(S1))      # 7
print(S1)           # {False, True, 67, 'Selenium', 'Rest_Assured', 'Debojyoti', 123.45}
print("================= Delete element from the set =================")
S1.remove("Debojyoti")
print(len(S1))      # 6
print(S1)           # {False, True, 67, 'Selenium', 'Rest_Assured', 123.45}
# S1.remove("Basu") # Will generate KeyError: 'Basu'
print("================= Delete element from the set other method =================")
S1.discard(False)
print(len(S1))      # 5
print(S1)           # {True, 67, 'Rest_Assured', 'Selenium', 123.45}
S1.discard("Basu")  # Will not generate KeyError: 'Basu'
print("================= Copy one set to another =================")
S2 = S1.copy()
print("Set S1: ", S1)
print("Set S2: ", S2)
print("================= Clear any set =================")
S1.clear()
print("Set S1 after clear: ", S1)
print("Set S2: ", S2)
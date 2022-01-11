# Python Flow Control

"""
1. If Statement
2. If Else Statement
3. If Elif Else Statement
4. For Loops
5. While Loops
6. Nested Loops
7. Break Statement
8. Continue Statement
9. Loops With Else Block
10. Pass Statment
"""

"""
1. If Statement
    If the "If" condition is true, python will run the code in If block, otherwise it will skip the If block
2. If Else Statement
    If the "Else" condition is true, python will run the code in Else block.
"""

a = 20
b = 30
if a > b:
    print(a)
    print('"a" is the biggest number')
else:
    print(b)
    print('"b" is the biggest number')
print("Outside the if block")

marks = int(input("Enter your math marks: "))
carrier = input("Enter future carrier: ")

if marks==100:
    if carrier == "Astrophysicist":
        print("Brilliant choice")
    else:
        print("Hmmm, Well, Best of luck")
    grade = "Outstanding Score"
    print(grade)
elif 80 < marks < 100:
    if carrier == "Doctor":
        print("Good choice")
    grade = "Excellent Score"
    print(grade)
elif 60 < marks < 80:
    if carrier != "Astrophysicist" or carrier != "Astrophysicist":
        print("Best Of Luck")
    grade = "Very Good Score"
    print(grade)
elif 40 < marks < 60:
    if carrier != "Astrophysicist" or carrier != "Astrophysicist":
        print("Then focus in your study")
    grade = "Satisfactory Score"
    print(grade)
elif 30 < marks < 40:
    grade = "Fail"
    print(grade)
    print("Surprise Me")
else:
    print("Beta Neta ban jao")


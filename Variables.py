"""
Python is a “Dynamically Coupled” language, where Java is a "Statically Coupled" language
Meaning: If the user needs to define a variable to hold some integer value,
there is no need to define “int” before the variable name.
Example: See below
"""
a = 10
print(a)

"""
Variable to start with an underscore (_) or an alphabet (a-z | A-Z) is a mandate.
User cannot start a variable using any other character available.
As an example, refer the below attached image.

All characters after the first character can be combination of _ (Underscore) , a-z, A-Z or 0-9.
Example: See below
"""
_a = 100
print(_a)

b = 200
print(b)

a0 = 300
print(a0)

a_ = 400
print(a_)

aA_9_ = 500
print(aA_9_)

"""
Except Underscore (_), any type of special character is not at all allowed while defining a variable.
Also, NO WHITESPACES are allowed between a variable.

Since every programming language has some predefined variables, also called “Keywords”,
the user cannot name his/her variable with the same name. e.g. "if", "print"

Variables are case-sensitive in nature. It means, “A” and “a” are different variables.
“A” is storing some value and “a” is storing some other value.
"""

If = 600
print(If)

Print = 700
print(Print)

"""
In Python, another special quality lists a great feature.
User can initialise multiple variables at a single time.
It means, the user can assign the same/different value to multiple variables in a single line of statement.
"""

aA = bB = cC = "Debojyoti"
print(aA)
print(bB)
print(cC)

Aa, Bb, Cc = 800, 900.23, "Basu"
print(Aa)
print(Bb)
print(Cc)

"""
ython gives the user a privilege to check the type of the data user inserts at run time.
A dedicated function performing the mentioned task is available in Python.
“type()” is the function which returns the type of the variable to the user.
"""

xX, yY, zZ = "Debojyoti", 3.142857142857143, 900
print(type(xX))
print(type(yY))
print(type(zZ))

"""
Q1: Define the Lexical Rule for Identifiers.
A1: The required Grammar rule for Identifiers is -

Identifier = (letter | “_”)(letter | digit | “_”)*

Here, letter - a-z | A-Z

_ - Underscore

digit - 0-9

Q2: Mention some Best Practices for declaring an Identifier.
A2: Few of the Best practices are mentioned below -
Always prefer using “camelCase” for defining any variable.
Class name to start with an “Uppercase” , rest all to start with “Lowercase”
Name a variable properly. “a = 10” is less prefered from “amount = 10”
Use “_” to separate two words. Eg - “this_Is_A_Variable”

Q3: How can the user test if the Identifier is a Keyword or not ?
A3: A dedicated class is available in the system to verify or test if the Identifier is a keyword or not.
“Keyword” is the class. Check below:

import keyword

print keyword.iskeyword("if")
print keyword.iskeyword("If")
"""
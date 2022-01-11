print("This is a String")
print('This is a String too')
a = "Debojyoti"
b = 'Basu'
print(a)
print(b)
print(a,b)

"""
This is a valid
multiple line
comment with double quote
"""

'''
This is also valid
multiple line
comment with single quote
'''

print('Netaji said "Give me blood, I will give you freedom"')
print("Lal Bahadur Shastri said 'Jai Jawan Jai Kisan'")

c = 'Hello ' \
    'World!!!' \
    ' My ' \
    'name is ' \
    '"Debojyoti Basu"'
print(c)

d = """Hello World!!!
I am new in 
Python"""
print(d)

print("This is a Debojyoti's \"MacBook Pro\" laptop")   # If you want to write single and double quote at a time

str1 = "Twinkle twinkle little star"
str2 = "             Twinkle twinkle little star         "
str3 = "Baa Baa Black Sheep"
print(str1[3])      # To get the 3rd index value
print(str1[3:9])    # To get the range of characters here from 3rd index to 8th index characters (before 9th char)
print(str1[3:9:1])  # Same as above with 1 char step jump
print(str1[3:9:2])  # Same as above with 2 chars step jump
print(str1[::])     # Entire characters with 1 step jump
print(str1[::2])    # Entire characters with 2 steps jump
print(str1[::-1])   # Reverse the string
print(len(str1))    # Length of the string
print(str2.strip()) # Strips left and right extra space
print(str1.lower()) # Lowercase of the string
print(str1.upper()) # Uppercase of the string

#Split the string and get the text Black from string str3
e = str3.split(" ")
print(e[2])

# Concatenation
f = "Debojyoti"
g = " Basu"
print(f + g)    # Concatenation could be possible with plus sign between same datatype

'''
i = 10
j = "Debojyoti"
print(i + j)    # Will not get any answer
'''

# Repetation
k = "10"
print(k * 4)    # 10 will print 4 times

l = "Ba"
m = "na"
print(l + m * 2)    # Maintaining BODMAS it will print Banana

# String Formatters
city = "Kolkata"
print("Hello, I live in ", city)

Age = 44
Id = 97760.64
# Want to print like: Hello, I live in Kolkata. My age is 44 and my ID is 97760
# Option 1
print(f"Hello, I live in {city}. My age is {Age} and my ID is {Id}.")
# Option 2
print("Hello, I live in {}, My age is {} and my id is {}.".format(city,Age,Id))
# Option 3
print("Hello, I live in %s, My age is %d and my id is %f."%(city,Age,Id))
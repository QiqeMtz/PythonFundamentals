str = 'programming'
print("str = ", str)

# first character accessing
print("str[0 = ", str[0])

# print last character
print("str[-1) = ", str[-1])

# slicing 2nd to 5th character
print("str[1:5) = ", str[1:5])

# slicing 6th to 2nd last character
print("str[5:-2) = ", str[5:-2])

# String operators
str1 = "Hello"
str2 = "World"

# concatenation using +
print("str1 + str2 = ", str1 + str2)

# concatenation using *
print("str1 * 3 = ", str1 * 3)

# concatenate in multiple lines with parenthesis
string2 = ("Hello"
    " world")

print(string2)

# Count the occurences of a letter in a string with a for loop
count = 0

for letter in "Hello World":
    if(letter == 'l'):
        count += 1

print(count, " letters 'l' found")

# triple quote
str = """He said, what's there?"""

print(str)

# escaping single quotes
str = "He said, what\'s there?"
print(str)

# escaping double quotes
str = "He said \"what's there?\""
print(str)

# examples
print("C:\\Python\\Lib")

print("This is printed \nin two lines")

print("This is \x48 \x45 \x58 representation")

# ignoring escape sequency with raw string
print("This is \x61 \ngood example")
print(r"This is a \x61 \ngood example")

# Formatting strings with Format() method
print("Binary representation of {0} is {0:b}".format(12))

# formating floats
print("Exponential representation of {0} is {0:e}".format(1566.345))

# round off
print("One third is {0:.3f}".format(1/3))

# String alignement
print("|{:<10}|{:^10}|{:>10}|".format("butter", "bread", "ham"))

# old printing
x = 12.3456789
print("The value of x is %3.4f" %x)

# Python string methods
print("PrOGrAMMinG".lower())

print("ProGRAmminG".upper())

str = "This is a phrase"
# Split a word into a list
listStr = str.split()

print(listStr)

# Join a list words into a String
print(" ".join(listStr))

str = "Happy birthday"
#replace a word of a string
print(str.replace("birthday", "halloween"))
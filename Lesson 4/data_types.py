import math

# STRING

# Literal assignment
first = 'Greg'
last = 'Gennaro'

# Print variable type
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatanation
fullName = first + " " + last
print(fullName)

fullName += "!!"
print(fullName)

# Cast a number to a string
year = str(1990)
print(type(year))

# Combine
sentence = "The book was written in the year " + year + "."
print(sentence)

# Multi-line String
multiline = '''
Hello! How are you?

This is a sample string.
                            <--- Indentations
'''
print(multiline)

# Escape Special Characters
sentence2 = 'I\'m learning Python!\tIt is fun.\n\nThis is a new line.'
print(sentence2)

# String Methods
print(first)
print(first.lower())
print(first.upper())

print(len(multiline)) # Length

print("")
# Build a menu
title = " menu ".upper()
print(title.center(20, "="))
print("Coffee ".ljust(16, ".") + "$1".rjust(4))
print("Bagel ".ljust(16, ".") + "$2".rjust(4))
print("Donut ".ljust(16, ".") + "$3".rjust(4))

print("")
print("")

# String Index Values
print(first[0]) # First Value
print(first[-1]) # Last Value
print(first[0:-1]) # Range: end of range is not included
print(first[0:]) # Range: to end of string

# String booleans
print(first.startswith("G"))
print(first.endswith("G"))

print("")
print("")
print("")


# BOOLEAN
myValue = True # Proper case
x = bool(False) # Constructor function
print(type(x))


# Numeric Data Types

# integer
price = 100
best_price = int(80)

# float
gpa = 3.87
y = float(1.14)

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1)) # Specify decimal

# Use Math module
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

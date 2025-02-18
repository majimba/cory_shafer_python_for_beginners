# Python Numbers Tutorial
# In Python, we have several numeric types:
# - int: Integer numbers (e.g., 3, -2, 1000)
# - float: Decimal point numbers (e.g., 3.14, -0.001, 2.0)

# Example of integer
num = 3
print(type(num))  # Output: <class 'int'>

# Example of float
num = 3.14
print(type(num))  # Output: <class 'float'>

# Arithmetic Operators in Python:
# These operators work with both integers and floats

# Addition: 3 + 2
# Returns the sum of two numbers
print(3 + 2)  # Output: 5

# Subtraction: 3 - 2
# Returns the difference between two numbers
print(3 - 2)  # Output: 1

# Multiplication: 3 * 2
# Returns the product of two numbers
print(3 * 2)  # Output: 6

# Division: 3 / 2
# Always returns a float in Python 3
print(3 / 2)  # Output: 1.5

# Floor Division: 3 // 2
# Returns the largest integer less than or equal to the division
print(3 // 2)  # Output: 1

# Exponent: 3 ** 2
# Raises the first number to the power of the second
print(3 ** 2)  # Output: 9

# Modulus: 3 % 2
# Returns the remainder of division
print(3 % 2)  # Output: 1

# Order of Operations (PEMDAS):
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(3 * 4 + 1)     # Output: 13 (multiplication happens first)
print(3 * (4 + 1))   # Output: 15 (parentheses take precedence)

# Variable Increment Methods:
num = 1
# Long form increment
num = num + 1
print(num)  # Output: 2

# Augmented assignment operator (shorthand)
num += 1
print(num)  # Output: 3

# Built-in Number Functions:
# abs(): Returns the absolute value
print(abs(-3))  # Output: 3

# round(): Rounds a number to specified decimals
print(round(3.75))    # Output: 4 (rounds to nearest integer)
print(round(3.75, 1)) # Output: 3.8 (rounds to 1 decimal place)

# Comparison Operators:
# These return boolean values (True/False)
num_1 = 3
num_2 = 2

# Equal to
print(3 == 2)  # Output: False

# Not equal to
print(3 != 2)  # Output: True

# Greater than
print(3 > 2)   # Output: True

# Less than
print(3 < 2)   # Output: False

# Greater than or equal to
print(3 >= 2)  # Output: True

# Less than or equal to
print(3 <= 2)  # Output: False

# Type Conversion (Casting):
# String to number conversion
num_3 = '100'
num_4 = '300'
print(num_3 + num_4)  # Output: '100300' (string concatenation)

# Converting strings to integers using int()
num_3 = int('100')
num_4 = int('300')
print(num_3 + num_4)  # Output: 400 (numeric addition)

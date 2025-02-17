# Python String Concatenation Tutorial
# This file demonstrates different methods to combine (concatenate) strings in Python

# Method 1: Using the + operator
# The + operator concatenates strings but can be inefficient for multiple strings
# Note: All operands must be strings, use str() to convert other types
greeting = "Hello"
name = "Majimba"

# Basic concatenation with + operator
message = greeting + ", " + name + ". " "Welcome!"  # Adjacent string literals are automatically concatenated
print(message)  # Output: Hello, Majimba. Welcome!

# Method 2: str.format() method
# Introduced in Python 2.6
# Uses {} as placeholders, filled by .format()
greeting = "Hello"
name = "Majimba"

# Using .format() method
# {} are replacement fields that get filled in order
# Can also use numbered {0}, {1} or named {greeting} placeholders
message = "{}, {}. Welcome!".format(greeting, name)
print(message)  # Output: Hello, Majimba. Welcome!


# Method 3: f-strings (Formatted string literals)
# Introduced in Python 3.6+
# Most readable and recommended method
# Allows direct embedding of expressions
greeting = "Hello"
name = "Majimba"

# Basic f-string usage
# Variables are directly referenced inside {}
message = f"{greeting}, {name}. Welcome!"
print(message)  # Output: Hello, Majimba. Welcome!

# Advanced f-string usage
# Can include expressions and method calls inside {}
greeting = "Hello"
name = "Majimba"

# Using methods inside f-string
message = f"{greeting}, {name.upper()}. Welcome!"  # Calls upper() method on name
print(message)  # Output: Hello, MAJIMBA. Welcome!

# Introspection Tools
# These help you explore string methods and functionality

# dir() function: Lists all attributes and methods of an object
greeting = "Hello"
name = "Majimba"

print(dir(name))  # Shows all available string methods

# help() function: Provides detailed documentation
# Note: These will open interactive help in terminal
print(help(str))          # Documentation for string class
print(help(str.lower()))  # Documentation for lower() method

# Additional String Concatenation Methods (Not shown in code):
# 1. Using join() method:
#    " ".join(['Hello', 'World'])  # Joins with space between
#
# 2. Using % operator (old style formatting):
#    "%s, %s" % (greeting, name)  # Not recommended for modern Python
#
# 3. Template strings from string module:
#    from string import Template
#    Template("$greeting, $name").substitute(greeting=greeting, name=name)

# Best Practices:
# 1. Use f-strings for simple concatenation (Python 3.6+)
# 2. Use join() for concatenating lists of strings
# 3. Use .format() if you need compatibility with Python < 3.6
# 4. Avoid + operator for multiple concatenations (inefficient)
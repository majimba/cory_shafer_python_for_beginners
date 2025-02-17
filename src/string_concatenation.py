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

# Additional String Concatenation Methods:

# Method 4: Using join() method
# Efficient for joining multiple strings, especially from a list
print("\nJoin Method Examples:")
# Basic join with space
words = ['Hello', 'World', 'from', 'Python']
message = " ".join(words)
print(message)  # Output: Hello World from Python

# Join with different delimiter
message = "-".join(words)
print(message)  # Output: Hello-World-from-Python

# Join with empty string (common for character lists)
chars = ['H', 'e', 'l', 'l', 'o']
message = "".join(chars)
print(message)  # Output: Hello

# Method 5: % operator (old style formatting)
# Not recommended for modern Python, but you might see it in old code
print("\n% Operator Examples:")
name = "Majimba"
age = 25
# Basic string formatting
message = "Hello, %s!" % name
print(message)  # Output: Hello, Majimba!

# Multiple values using tuple
message = "Hello, %s! You are %d years old." % (name, age)
print(message)  # Output: Hello, Majimba! You are 25 years old.

# Method 6: Template strings
# Useful for user-supplied strings or when you want to separate template from values
print("\nTemplate String Examples:")
from string import Template

# Basic template
template = Template("$greeting, $name!")
message = template.substitute(greeting="Hello", name="Majimba")
print(message)  # Output: Hello, Majimba!

# Template with dictionary
values = {'greeting': 'Hi', 'name': 'Majimba', 'message': 'Welcome'}
template = Template("$greeting, $name! $message")
message = template.substitute(values)
print(message)  # Output: Hi, Majimba! Welcome

# Safe substitution (doesn't raise KeyError for missing keys)
template = Template("$greeting, $name!")
message = template.safe_substitute(greeting="Hello")  # 'name' is missing
print(message)  # Output: Hello, $name!

# Introspection Tools
# These help you explore string methods and functionality

# dir() function: Lists all attributes and methods of an object
greeting = "Hello"
name = "Majimba"

print("\nAvailable String Methods:")
print(dir(name))  # Shows all available string methods

# help() function: Provides detailed documentation
# Note: These will open interactive help in terminal
print(help(str))          # Documentation for string class
print(help(str.lower()))  # Documentation for lower() method

# Best Practices:
# 1. Use f-strings for simple concatenation (Python 3.6+)
# 2. Use join() for concatenating lists of strings
# 3. Use .format() if you need compatibility with Python < 3.6
# 4. Avoid + operator for multiple concatenations (inefficient)
# 5. Use Template strings when dealing with user-supplied templates
# 6. Avoid % operator unless maintaining legacy code
# Python String Methods Tutorial
# Strings in Python are immutable sequences of characters. This means once a string is created,
# it cannot be modified. All string methods return new strings rather than modifying the original.

# Create our sample string
# Strings can be defined using single quotes ('') or double quotes ("")
message = "Hello World"

# print(): Built-in function that displays text to the console
# Syntax: print(value(s))
print(message)

# upper(): Converts all characters in the string to uppercase
# Returns: New string with all characters in uppercase
# Example: "hello" -> "HELLO"
print(message.upper())

# lower(): Converts all characters in the string to lowercase
# Returns: New string with all characters in lowercase
# Example: "HELLO" -> "hello"
print(message.lower())

# count(substring): Counts how many times a substring appears in the string
# Parameters: substring - The string to search for
# Returns: Integer representing the count of non-overlapping occurrences
# Example: "hello hello".count("he") returns 2
print(message.count("l"))

# find(substring): Searches for a substring and returns its starting position
# Parameters: substring - The string to search for
# Returns: Index of first occurrence (0-based) or -1 if not found
# Example: "Hello".find("e") returns 1
print(message.find("World"))

# replace(old, new): Substitutes all occurrences of one substring with another
# Parameters: 
#   old - The substring to be replaced
#   new - The substring to replace with
# Returns: New string with all replacements made
# Example: "Hello World".replace("World", "Python") returns "Hello Python"
print(message.replace("World", "Universe"))

# split([separator]): Breaks a string into a list of substrings
# Parameters: separator (optional) - The delimiter to split on
# Returns: List of strings
# If no separator is specified, splits on whitespace (spaces, tabs, newlines)
message = "Hello, how arre you doing today?"
words = message.split()  # Split on whitespace
print(words)

# split() with custom delimiter
# Common use case: Parsing CSV (Comma-Separated Values) data
csv_line = "Majimba,Majimba,37,Engineer"
values = csv_line.split(",")  # Split on commas
print(values)

# String whitespace removal methods:
# strip(): Removes leading and trailing whitespace (or specified characters)
# lstrip(): Removes leading whitespace (from left side)
# rstrip(): Removes trailing whitespace (from right side)
# Whitespace includes: spaces, tabs, newlines
message = "   Hello World   "
print(message.strip())     # Removes both leading and trailing spaces
print(message.lstrip())    # Only removes leading spaces
print(message.rstrip())    # Only removes trailing spaces

# join(): Combines a list of strings into a single string
# Syntax: delimiter.join(iterable)
# The string on which join() is called becomes the delimiter between elements
# Parameters: iterable - A sequence of strings to join together
# Returns: Single string with all elements joined
words = ["Hello", "World", "from", "Python"]
sentence = " ".join(words)     # Join with space: "Hello World from Python"
print(sentence)

# join() with different delimiter
csv = ",".join(words)          # Join with comma: "Hello,World,from,Python"
print(csv)

# String prefix and suffix checking methods:
# startswith(): Checks if string begins with specified prefix
# endswith(): Checks if string ends with specified suffix
# Both return: Boolean (True/False)
message = "Hello World"
print(message.startswith("Hello"))    # True - string starts with "Hello"
print(message.endswith("World"))      # True - string ends with "World"

# Case manipulation methods:
# capitalize(): Makes first character uppercase, rest lowercase
# title(): Capitalizes first character of each word
# Example: "hello world" -> "Hello world" (capitalize)
# Example: "hello world" -> "Hello World" (title)
txt = "hello world, welcome to python!"
print(txt.capitalize())   # Only first letter of string is capitalized
print(txt.title())       # First letter of each word is capitalized

# Substring search methods:
# find(): Searches forward from beginning of string
# rfind(): Searches backward from end of string
# Both return: Index of substring or -1 if not found
txt = "hello World, welcome to the world of Python!"
index = txt.find("welcome")        # Returns index of first 'welcome'
print(index)
last_index = txt.rfind("world")    # Returns index of last 'world'
print(last_index)

# replace(): String substitution method
# Parameters:
#   old - substring to find
#   new - substring to replace with
#   [count] - optional, maximum number of replacements to make
# Returns: New string with replacements
txt = "hello World, welcome to the World!"
new_txt = txt.replace("World", "Universe")  # Replaces all occurrences
print(new_txt)

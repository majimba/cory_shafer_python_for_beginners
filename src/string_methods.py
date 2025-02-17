# String Methods in Python
# This file demonstrates various string manipulation methods available in Python

# Store our message in a variable
message = "Hello World"

# print(): Outputs the string to the console
print(message)

# upper(): Returns a new string with all characters converted to uppercase
print(message.upper())

# lower(): Returns a new string with all characters converted to lowercase
print(message.lower())

# count(substring): Returns the number of occurrences of a substring in the string
print(message.count("l"))

# find(substring): Returns the index of the first occurrence of the substring
# Returns -1 if the substring is not found
print(message.find("World"))

# replace(old, new): Returns a new string where all occurrences of 'old' are replaced with 'new'
print(message.replace("World", "Universe"))

# split([separator]): Splits the string into a list of substrings based on the separator
# If no separator is specified, splits on whitespace
message = "Hello, how arre you doing today?"
words = message.split()
print(words)

# split() with custom delimiter: Splits the string using the specified character
csv_line = "Majimba,Majimba,37,Engineer"
values = csv_line.split(",")
print(values)

# strip(): Removes leading and trailing whitespace (or specified characters)
# lstrip(): Removes leading whitespace
# rstrip(): Removes trailing whitespace
message = "   Hello World   "
print(message.strip())    # Removes whitespace from both sides
print(message.lstrip())   # Removes whitespace from left side
print(message.rstrip())   # Removes whitespace from right side

# join(): Combines a list of strings into a single string using the specified delimiter
# The string on which join() is called becomes the delimiter
words = ["Hello", "World", "from", "Python"]
sentence = " ".join(words)    # Using space as delimiter
print(sentence)

# join() with different delimiter
csv = ",".join(words)         # Using comma as delimiter
print(csv)

# startswith(): Returns True if the string starts with the specified prefix
# endswith(): Returns True if the string ends with the specified suffix
message = "Hello World"
print(message.startswith("Hello"))    # Check if string starts with "Hello"
print(message.endswith("World"))      # Check if string ends with "World"

# capitalize(): Converts the first character to uppercase and the rest to lowercase
# title(): Converts the first character of each word to uppercase
txt = "hello world, welcome to python!"
print(txt.capitalize())   # Capitalizes first letter of string
print(txt.title())       # Capitalizes first letter of each word

# find(): Returns the lowest index of the substring if found
# rfind(): Returns the highest index of the substring if found
# Both return -1 if substring is not found
txt = "hello World, welcome to the world of Python!"
index = txt.find("welcome")       # Find first occurrence
print(index)
last_index = txt.rfind("world")   # Find last occurrence
print(last_index)

# replace(): Creates a new string by replacing all occurrences of a substring
txt = "hello World, welcome to the World!"
new_txt = txt.replace("World", "Universe")
print(new_txt)

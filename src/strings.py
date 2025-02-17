# Python Strings Tutorial
# Strings are immutable sequences of characters in Python
# They can be created using single quotes ('') or double quotes ("")

# String Creation: Double Quotes
# Use double quotes when the string contains single quotes
message = "Hello World"
print(message)

# String Creation: Single Quotes
# Use single quotes when the string contains double quotes
message = 'Hello World'
print(message)

# Escape Characters
# Use backslash (\) to include special characters in strings
# Common escape sequences:
# \' - Single quote
# \" - Double quote
# \n - Newline
# \t - Tab
message = 'Bobby\'s World'    # Using \' to include apostrophe in single-quoted string
print(message)

# Multi-line Strings
# Use triple quotes (''' or """) for strings that span multiple lines
# Preserves all whitespace and line breaks
message = """
I love me 
some Majimba
"""
print(message)

# String Length
# len() is a built-in function that returns the number of characters
txt = "I love you"
print(len(message))    # Counts all characters including whitespace and newlines

# String Indexing and Slicing
# Strings are sequences and can be accessed by index
# Positive indices start from 0
# Negative indices start from -1 (last character)
msg = "Hello World"
print(msg[0])      # Output: 'H' (first character)
print(msg[:5])     # Output: 'Hello' (first five characters)
print(msg[6:])     # Output: 'World' (from 6th character to end)

# Video: https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2&ab_channel=CoreySchafer
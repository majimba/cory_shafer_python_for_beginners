# Practical String Manipulation Examples in Python
# This script demonstrates common string operations in real-world scenarios
# Each example shows how to solve practical text processing tasks

# Original Message with extra whitespace
# Note: The string has leading and trailing spaces that we'll clean up
message = "    Hello, how are you doing today?    "

# Example 1: Word Tokenization
# Problem: Split a sentence into individual words
# Solution: Use strip() to remove extra whitespace, then split() to separate words
# strip() removes both leading and trailing whitespace (spaces, tabs, newlines)
# split() without arguments splits on any whitespace character
words = message.strip().split()
print("Words:", words)  # Output: ['Hello,', 'how', 'are', 'you', 'doing', 'today?']

# Example 2: Text Reconstruction
# Problem: Join words back into a properly formatted sentence
# Solution: Use join() with a space as the delimiter
# join() is called on the delimiter and takes an iterable of strings as argument
sentence = " ".join(words)
print("Sentence:", sentence)  # Output: "Hello, how are you doing today?"

# Example 3: String Pattern Matching
# Problem: Check if text starts or ends with specific phrases
# startswith(): Checks beginning of string
# endswith(): Checks end of string
# Both methods return True/False and are case-sensitive
print("Starts with 'Hello':", sentence.startswith("Hello"))  # True
print("Ends with '?':", sentence.endswith("?"))             # True

# Example 4: Text Case Formatting
# Problem: Format text for different display purposes
# capitalize(): Makes first letter uppercase, rest lowercase
# title(): Capitalizes first letter of each word (Title Case)
print("Capitalized:", sentence.capitalize())  # Only first letter of sentence
print("Title-case:", sentence.title())        # First letter of each word

# Example 5: Substring Search
# Problem: Find the position of a word in text
# find(): Returns the index where the substring starts
# Returns -1 if substring is not found
# Note: Index is 0-based (first character is at position 0)
index_how = sentence.find("how")
print("Index of 'how':", index_how)  # Shows where 'how' begins in the sentence

# Example 6: Text Replacement
# Problem: Replace specific words in a sentence
# replace(old, new): Substitutes all occurrences of 'old' with 'new'
# Creates a new string (original string is unchanged)
new_sentence = sentence.replace("today", "tonight")
print("Replaced sentence:", new_sentence)  # 'today' becomes 'tonight'

# Note: String Immutability
# Remember: In Python, strings are immutable (cannot be changed in place)
# Methods like replace(), strip(), etc. always return new strings
# Original string remains unchanged unless you reassign the variable
# Original Message
message = "    Hello, how are you doing today?    "


# Split message into words
words = message.strip().split()
print("Words:", words)

# Join the words back into a sentence with a space
sentence = " ".join(words)
print("Sentence:", sentence)

# Check how a sentence starts and ends
print("Starts with 'Hello':", sentence.startswith("Hello"))
print("Ends with '?':", sentence.endswith("?"))

# Capitalize and title-case the sentence
print("Capitalized:", sentence.capitalize())
print("Title-case:", sentence.title())

# Find substring positions
index_how = sentence.find("how")
print("Index of 'how':", index_how)

# Replace a substring
new_sentence = sentence.replace("today", "tonight")
print("Replaced sentence:", new_sentence)
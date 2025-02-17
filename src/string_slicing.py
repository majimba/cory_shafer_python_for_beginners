# Python String and List Slicing Tutorial
# Slicing allows you to extract parts of sequences (lists, strings) using the syntax:
# sequence[start:end:step]
# - start: First index to include (default: 0)
# - end: First index to exclude (default: length of sequence)
# - step: Number of items to skip (default: 1)

# Example list with positive and negative indices
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Positive indices:  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Negative indices:-10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# Basic indexing
# Accessing single elements using positive and negative indices
print(my_list[5])     # Output: 5 (sixth element)
print(my_list[-1])    # Output: 9 (last element)
print(my_list[-10])   # Output: 0 (first element from end)

# Basic slicing with positive indices
# Syntax: list[start:end] - includes start, excludes end
print(my_list[0:6])   # Output: [0, 1, 2, 3, 4, 5]
print(my_list[3:8])   # Output: [3, 4, 5, 6, 7]

# Slicing with negative indices
# Negative indices count from the end of the sequence
print(my_list[-7:-2])  # Output: [3, 4, 5, 6, 7]
print(my_list[1:-2])   # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Omitting indices
# If start is omitted, slice starts from beginning
# If end is omitted, slice goes to end
print(my_list[1:])     # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[:-1])    # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(my_list[:])      # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (creates a copy)

# Slicing with step
# step > 0: Move forward through sequence
# step < 0: Move backward through sequence
print(my_list[2:-1:2])   # Output: [2, 4, 6, 8] (every second element)
print(my_list[-1:2:-1])  # Output: [9, 8, 7, 6, 5, 4, 3] (backwards)

# Reversing a sequence
# Using [::-1] is a common idiom to reverse a sequence
print(my_list[::-1])     # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Practical Example: URL Manipulation
sample_url = "http://coreyms.com"
print(sample_url)

# Reverse the URL (useful for testing string manipulation)
print(sample_url[::-1])  # Output: moc.smyeroc//:ptth

# Extract the top-level domain (.com)
# Using negative slice to get last 4 characters
print(sample_url[-4:])   # Output: .com

# Remove the protocol (http://)
# Start from index 7 (after "http://")
print(sample_url[7:])    # Output: coreyms.com

# Get the domain name without protocol or TLD
# Combine positive and negative slicing
print(sample_url[7:-4])  # Output: coreyms

# Reference: https://www.youtube.com/watch?v=ajrtAuDg3yw

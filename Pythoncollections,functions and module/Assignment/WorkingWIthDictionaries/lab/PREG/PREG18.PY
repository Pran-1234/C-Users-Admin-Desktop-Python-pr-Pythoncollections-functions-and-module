# Sample string
my_string = "hello world"

# Creating an empty dictionary to store the character count
char_count = {}

# Iterating through each character in the string
for char in my_string:
    # If the character is already in the dictionary, increment its count
    if char in char_count:
        char_count[char] += 1
    # Otherwise, add the character to the dictionary with count 1
    else:
        char_count[char] = 1

# Printing the character count
print("Character count:", char_count)

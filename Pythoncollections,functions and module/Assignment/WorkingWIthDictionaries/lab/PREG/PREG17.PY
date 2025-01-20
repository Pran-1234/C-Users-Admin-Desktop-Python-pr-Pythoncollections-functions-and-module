# Sample lists
keys = ['a', 'b', 'c', 'd']
values = [10, 20, 30, 40]

# Converting lists into a dictionary using a for loop
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

# Printing the dictionary
print("Dictionary:", my_dict)

# Two lists
keys = ['name', 'age', 'city']
values = ['PRAN', 22, 'ABC']

# Initialize an empty dictionary
merged_dict = {}

# Using a loop to merge lists into a dictionary
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

# Output the merged dictionary
print(merged_dict)

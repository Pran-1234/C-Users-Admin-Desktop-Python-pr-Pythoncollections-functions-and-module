#multiple data types
# Creating a tuple with multiple data types
my_tuple = (42, "hello", 3.14, True, [1, 2, 3], {"key": "value"}, (5, 6))

# Printing the tuple
print("Tuple with multiple data types:", my_tuple)

# Accessing each element to show data types
for i, element in enumerate(my_tuple):
    print(f"Element {i}: {element} (Type: {type(element)})")

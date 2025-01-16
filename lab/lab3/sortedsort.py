# Sample list
my_list = [12, 5, 3, 19, 7, 2, 8]

# Using sort() - modifies the original list
print("Original list:", my_list)
my_list.sort()  # In-place sorting
print("List after using sort():", my_list)

# Using sorted() - returns a new sorted list
my_list = [12, 5, 3, 19, 7, 2, 8]  # Reset the original list
sorted_list = sorted(my_list)  # Create a new sorted list
print("List after using sorted():", sorted_list)

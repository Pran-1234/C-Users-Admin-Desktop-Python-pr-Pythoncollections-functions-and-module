#creating empty list
# Initialize an empty list
my_list = []

# Specify the number of elements to insert
num_elements = int(input("Enter the number of elements to insert: "))

# Use a for loop to insert elements into the list
for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

# Print the final list
print("The final list is:", my_list)

# Creating a dictionary
my_dict = { 'name': 'Pranali','age': 22,'city': 'Ahmedabad', 'profession': 'Engineer','hobby': 'Reading'}
print("Accessing values using keys:")
print("Name:", my_dict['name'])  
print("Age:", my_dict['age'])  
print("City:", my_dict['city'])  

print("\nAccessing values using get() method:")
print("Profession:", my_dict.get('profession'))  
print("Hobby:", my_dict.get('hobby'))          
print("\nAccessing a key that doesn't exist using get():")
print("Country:", my_dict.get('country', 'Key not found')) 
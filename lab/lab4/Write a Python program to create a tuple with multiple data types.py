#Write a Python program to create a tuple with multiple data types.
my_tuple=(2,3.12,"hello",True,[1,2,3],{"key":"value"},(5,6))
print("Listed tuple:",my_tuple)
for i,element in enumerate(my_tuple):
     print(f"Element {i}: {element} (Type: {type(element)})")
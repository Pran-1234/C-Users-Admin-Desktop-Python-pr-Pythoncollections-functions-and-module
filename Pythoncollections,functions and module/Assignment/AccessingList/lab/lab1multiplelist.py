#Write a Python program to create a list with elements of multiple data types (integers,
#strings, floats, etc.).
def mix():
    mixed_list = [42, 3.14, "Hello", True, None]
    for element in mixed_list:
           print(f"Element: {element}, Type: {type(element)}")
mix()
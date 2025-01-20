mixed_list=[42,"Hello",3.14,True,None,[1,2,3],{"Name:Pranali"},(4,5),{7,8,9}]
print("Mixed data type list:",mixed_list)
print("Elements and their data types")
for element in mixed_list:
    print(f"{element}-{type(element)}")


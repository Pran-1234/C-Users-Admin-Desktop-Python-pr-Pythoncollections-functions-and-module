#Write a Python program to remove elements from a list using pop() andremove().
list2=[10,20,30,40,50,60,70,90]
res=list2.remove(30)
print("after removing:",res)
print(list2)
res1=list2.pop()
print("after popping:",res1)
print(list2)
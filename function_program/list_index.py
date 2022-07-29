# python program to find the index of an element :

a=[]
for i in range(int(input("enter the numbers  you want to range :"))):
    x=input("enter the list name :") # this is string so use only input

    a.append(x)
print(a)  
# we want to find the element index that provide in a list :
z=input("enter the element name you want to find index :")
print("index of element = ",a.index(z))  

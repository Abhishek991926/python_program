# program to use remove method in a list 
# we can remove anything in a list with their name 

a=[]
for i in range(int(input("enter the numbers  you want to find range  : "))):
    x=input("enter the list element   :")
    a.append(x)
print("original list = ",a)


# enter the element you want to remove 

b=input("enter the element name you want to remove  :")
a.remove(b)
print(" remove element name = ",a)
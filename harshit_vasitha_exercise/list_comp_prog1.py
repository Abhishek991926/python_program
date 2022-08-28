#!/usr/bin/env python
# write a program to print square of given range using list comp


square=[i**2 for i in range(1,int(input("enter the range : ")))]
print(square)



# reverse of the string :

l1=["abhishek","aman","satyam"]
l2=[]
for i in l1:
    l2.append(i[::-1])
print(l2)         
    


# this program is used using list comp

a=[]
for i in range(int(input("enter the range you want : "))):
    x=input("enter the list elements : ")
    a.append(x)
print(a)   

a2=[i[::-1] for i in a]
print(a2)
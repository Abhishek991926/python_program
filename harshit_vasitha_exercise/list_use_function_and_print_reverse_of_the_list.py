# program to print reverse the list element that position :

from re import A


def reverse_list(l):
    a=[]
    for i in range(len(l)):
        a.append(l[i][::-1])
    return a


l2=[]
for i in range(int(input("enter the range : "))):
    x=input("enter the list element : ") 
    l2.append(x)
print(l2)

print(reverse_list(l2))
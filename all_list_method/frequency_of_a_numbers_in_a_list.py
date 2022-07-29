# program to find the frequency of a numbers in a given list:

a=[]
for i in range(int(input("enter the numbers :"))):
    x=int(input("enter the numbers you wand to append in the list : "))
    a.append(x)
print("original list = ",a)
num=int(input("enter the numbers : "))
#for i in range(len(a)):
c=a.count(num)
print("frequency of numbers = ",c)    

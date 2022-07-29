# program to find the max of the list using max functions :

a=[]
for i in range(int(input("enter the range : "))):
    x=int(input("enter the numbers to append the list : "))
    a.append(x)
print("my list = ",a)  
print("max of the list = ",max(a))


#2nd method without using max functions :

max=a[0]
for i in range(len(a)):
    if(a[i]>max):
        min=a[i]
print("max of the list = ",max)        
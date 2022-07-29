# take a list and print square of the list 


a=[]
for i in range(int(input("enter the range : "))):
    x=int(input("enter the numbers :"))
    a.append(x)
print(a) 

z=[]

for i in range(len(a)):
    z.append(a[i]**2)
print(z)
# TAKE  a list and return reverse of the list :

a=[]
for i in range(int(input("enter the range : "))):
    x=int(input("enter the numbers : "))
    a.append(x)

print(a)  

n=len(a)

for i in range(n//2):
    a[i],a[n-i-1]=a[n-i-1],a[i]


print(a)    



# method second 

    

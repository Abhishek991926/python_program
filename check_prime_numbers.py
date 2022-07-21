# program to check a given number is prime or not 

# logic 
# if a numbers is exactly two factors  This numbers is prime 

num=int(input("enter the numbers :"))
count=0
i=1
while(i<=num):
    if(num%i==0):
        count+=1
    i+=1
if(count==2):
    print("prime")
else:
    print("composite")            

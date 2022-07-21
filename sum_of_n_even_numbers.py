# write a program to find sum of n even numbers :

#method1 

n=int(input("enter the numbers :"))
i=2
sum=0
count=0
while(count<n):
    sum+=i
    count+=1
    i+=2
print("sum of even numbers =",sum)   


# method 2nd

n1=int(input("enter the numbers :"))
i=1
sum=0
count=0
while(count<n1):
    if(i%2==0):
        sum+=i
        count+=1
    i+=1
print("sum of even numbers = ",sum)        
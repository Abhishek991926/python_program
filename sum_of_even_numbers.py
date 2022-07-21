# write a program to find sum of even numbers 

# method 1

from re import I


num=int(input("enter the numbers :"))
i=2 
sum=0
while(i<=num):
    sum+=i 
    i+=2
print("sum of even numbers = ",sum)      



# method 2nd

num1=int(input("enter the numbers :"))
i=1
sum=0
while(i<=num1):
    if i%2==0:
        sum+=i
    i+=1
print("sum of even numbers = ",sum)        
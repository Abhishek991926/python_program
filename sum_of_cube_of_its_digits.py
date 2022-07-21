# program to find sum of cube of its digit 

# method 1

num1=input("enter the numbers :")
i=0
sum=0
while(i<len(num1)):
    sum+=int(num1[i])**3
    i+=1
print("sum of cube of its digit = ",sum)      


# method 2nd 
# logical method 

num2=int(input("enter the numbers :"))
sum=0
while(num2>0):
    sum+=(num2%10)**3
    num2=num2//10
print("sum of cube of its digit = ",sum)    
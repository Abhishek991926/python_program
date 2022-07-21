# program to find sum of square of its digit

# method 1

num=input("enter the digits :")

i=0
sum=0
while(i<len(num)):
    sum+=int(num[i])**2
    i+=1
print("sum of square of its digit= ",sum)    


# method 2

num=int(input("enter The digits :"))
sum=0
while(num>0):
    sum+=(num%10)*(num%10)
    num=num//10

print("sum of square of its digit= ",sum)    
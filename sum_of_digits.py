num=input("enter the  numbers :")

i=0
sum=0
while(i<len(num)):
    sum+=int(num[i])
    i+=1
print(sum)    


# method 2nd 

num=int(input("enter the numbers :"))

sum=0
while(num>0):
    sum+=(num%10)
    num=num//10
print("sum of digit = ",sum)    
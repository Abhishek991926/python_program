num=int(input("enter the numbers :"))
num1=num
count=0
while(num1>0):
    num1=num1//10
    count+=1
num1=num
sum=0
while(num1>0):
    digit=num1%10
    i=1
    product=1
    while(i<=count):
        product=digit*product
        i+=1
    sum+=product
    num1=num1//10
if (sum==num):
    print("armstrong numbers ")
else:
    print("not armstrong")            

  
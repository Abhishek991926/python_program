# program to find product of digit
# method 1


num=input("enter the numbers :")
i=0
pro=1
while(i<len(num)):
    pro*=int(num[i])
    i+=1
print(pro)    


n=int(input("enter the numbers :"))
pro=1
while(n>0):
    pro*=(n%10)
    n=n//10
print("product of digit = ",pro)    
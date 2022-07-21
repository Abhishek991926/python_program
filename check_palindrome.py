num=int(input("enter the numbers :"))
n=num
rev=0
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
    

if(num==rev):
    print("palindrome")
else:
    print("not palindrome")        
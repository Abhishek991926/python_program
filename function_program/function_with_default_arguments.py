# make a program to use default arguments :

def add(a,b,c=5):  # when no any argument pass in c then it will take 5
# when pass the value of c in this program then default value is null    
    return a+b+c
num1=int(input("enter the  first number :"))
num2=int(input("enter the second number : "))
#num3=int(input("enter the third number : "))


print(add(num1,num2))  
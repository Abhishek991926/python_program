# function with no arguments and no return 

def add():
    a=int(input("enter the first numbers :"))
    b=int(input("enter the second numbers :"))
    c=a+b
    print("Addition = ",c)
add()    


# function with arguments and without return:

def odd_even(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")
odd_even(int(input("enter the numbers ")))


# function not arguments but return :

def add():
    a=int(input("enter the numbers "))
    b=int(input("enter the second numbers :"))

    return a+b
print(add())    


# function with argument and return 


def add(a,b):
    return a+b

x=int(input("enter the first numbers :")) 
y=int(input("enters the second numbers :"))
print(add(x,y))   


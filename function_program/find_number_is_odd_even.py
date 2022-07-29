# program to find function is odd or even using functions


# make the program without arguments :

def odd_even():
    a=int(input("enter the numbers :"))
    if(a%2==0):
        print("number is even ")
    else:
        print("number is odd") 
odd_even()    


# make program with arguments :

def odd_even(a):
    if(a%2==0):
        print("number is even")
    else:
        print("number is odd")
odd_even(int(input("enter the number :")))


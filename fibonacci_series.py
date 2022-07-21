# python program to print fibonacci series 


num=int(input("enter the numbers :"))
x=0
y=1
z=0
while(z<=num):
    print( z,end=" ")
    x=y
    y=z
    z=x+y
# python program to print square of a list from 1 to 10 numbers :

square=[]
for i in range(int(input("enter the range : "))):
    square.append(i**2)
print(square)      


# using functions :

def square_list(num):
    square=[]
    for i in range(1,num):
        square.append(i**2)
    return square

num=int(input("enter the numbers : "))
print(square_list(num))

            
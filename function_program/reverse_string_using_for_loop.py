# python program to reverse the string using for loop:

a=input("enter the string")
print(a[::-1])


# but using for loop 

b=input("enter the string  :")
for i in range(len(b)-1,-1,-1):
    print(b[i],end="")
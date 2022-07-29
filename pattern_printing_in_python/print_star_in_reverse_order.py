# print star in reverse order 

# *****
# ****
# ***
# **
# *

num=int(input("enter the numbers :"))
i=num
while(i>0):
    j=1
    while(j<=i):
        print("*",end=" ")
        j+=1
    print()    
    i=i-1    
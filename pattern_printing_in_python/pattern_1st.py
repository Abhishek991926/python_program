# python program to print star at right angle triangle 

# *
# **
# ***
# ****
# *****

num=int(input("enter the numbers :"))
i=1
while(i<=num):
    j=1
    while(j<=i):
        print("*",end="")
        j+=1
    print()    
    i+=1

# 2nd print 

# 1
# 22
# 333
# 4444
# 55555

num=int(input("enter the numbers :"))
i=1
while(i<=num):
    j=1
    while(j<=i):
        print(i,end="")
        j+=1
    print()
    i+=1    

        

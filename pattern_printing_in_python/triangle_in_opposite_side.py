# pattern print 

#      * # in this section we want to count space 
#     **
#    ***
#   ****

num=int(input("enter the numbers :"))
i=1
while(i<=num):
    x=1
    while(x<=num-i):
        print("  ",end="")
        x+=1
    j=1
    while(j<=i):
        print("*",end=" ")
        j+=1
    print()
    i+=1    

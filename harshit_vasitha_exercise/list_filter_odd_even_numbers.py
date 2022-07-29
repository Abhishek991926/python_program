# define a function that take a list and filter the odd and even numbers 

#example :

# [1,2,3,4,5,6,7,8,9] >>>>>>[[1,3,5,7,9],[2,4,6,8]]
# 
l1=[1,2,3,4,5,6,7,8,9,10]
l3=[]
l4=[]
for i in l1:
    if(i%2==0):
        l3.append(i)
    else:
        l4.append(i) 
output=[l4,l3]           
print(l3)        
print(l4)  
print(output) 

# using function 

def filter_odd_even(l):
    l1=[]
    l2=[]
    for i in l:
        if(i%2==0):
            l1.append(i)
        else:
            l2.append(i)
    output=[l2,l1]
    return output
z=[]
for j in range(int(input("enter the rannge :"))):
    x=int(input("enter the list element : "))
    z.append(x)
print(filter_odd_even(z))    

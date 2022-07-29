# python program to find total odd and even numbers present in the list :

# simple program using input 

a=[1,2,3,4,5,6,7,8]
even=0
odd=0
for i in a:
    if(i%2==0):
        even+=1
    else:
        odd+=1

print("total even numbers = ",even)
print("total odd = ",odd)            
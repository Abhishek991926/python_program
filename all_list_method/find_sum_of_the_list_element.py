# program to find sum of the list element :

# given list 
a=[1,23,4,5,6,7]
sum=0
for i in a:
    sum+=i
print("sum of the list = ",sum) 



# take input by users :

a=[]
for i in range(int(input("enter the element you want to range : "))):
    x=int(input("enter the element to append in the list : "))
    a.append(x)
print(a)   
sum=0
for j in a:
    sum+=j
print("sum of the list = ",sum)   


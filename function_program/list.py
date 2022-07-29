# list is a collection of different values and different item 
# we can delete any item in a list 
# we can assign any item in a list 
# list are muttable 


# program in list 

# list store any data type 

a=["abhishek",1,'aman',"satyam",12.5]
print(a)


# list slicing

print(a[0])

print(a[:3])

print(a[-1::-2])

# list using assignment operator 

a[0]="sanjay"
print(a)


# how to delete any item in a list 


del(a[0])
print(a)

c=a.index("satyam")
print(c)

del(a[2])
print(a)

# we are creating a list 

b=["abhishek","aman","satyam",1,2,3,4,5,8.9]
for i in b:
    print(i,end=" ")

for i in range(len(b)):
    print(b[i],end=" ")    
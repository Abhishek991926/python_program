# first method is len(function)
# in this function we are find the length of the list 

a=["abhishek","aman",1,2,3,4,45.87]
print(len(a))

a=[]
for i in range(int(input("enter the range you want : "))):
    x=input("enter the list element : ")
    a.append(x)
print("original list = ",a)
print("length of the list = ",len(a))


# using max function this function is return the maximum value of the list 

print("max of the list = ",max(a))

# min of the list :
# the min method are used to find the minimum value of the list 

print("min of the list = ",min(a))

# append method 
# this method are used to append the element in the last of the list :

z=input("enter the element you want to append : ")
a.append(z)
print("using append method the list id = ",a)

# count method 
# this method is used to count a specifice element that are present in the list 

k=input("enter the count element : ")
print("count element in the list = ",a.count(k))

# index method 
# index method are used to find the position of the element in the list 

s=input("enter the elemrnt name you want to find index : ")
print("index of element in the list = ",a.index(s))

# insert method 
# this method is used to insert the element in the list with given position

v=input("enter the element name you want to insert : ")
a.insert(2,v)
print("after insertion the list is = ",a)

# remove method 
# this method are used to remove the specifice element in the list 

c=input("enter the element name you want to remove : ")
a.remove(c)
print("list after remove = ",a)

# pop method 
# this method are used to delete the last element of the list 

a.pop()
print(a)

# method to insert the list :
# append 
# insert 
# extend 

# method to delete the element in the list
# del 
# pop
# remove 

# method to find the  length of the element in the list 

# using len() function

# method to count the element in the list 
# use count()method 

#method to sort the list use :
# sort() method   
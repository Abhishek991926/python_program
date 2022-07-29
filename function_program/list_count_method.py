# in a list count method count the frequency of an element
# that present in a list 

# count method count the occurence of an element in a list :


name=["abhishek",'satyam','aman','abhishek','abhishek']
print(name.count('abhishek'))
print(name.index('abhishek'))



# 

a=[]
for i in range(int(input("enter the range you want :" ))):
    x=input("enter the name :")
    a.append(x)
print(a) 
x=input("enter the value you want to count")
print("frequency = ",a.count(x))



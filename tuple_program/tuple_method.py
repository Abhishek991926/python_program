# in tuple we use the method are :

t1=(1,2,3,4,5)
print(t1) 

# method 1 max()

print(max(t1)) # max method the value which have maximum in numbers :

print(min(t1)) # give minimum value present in the tuple :

# method 3 len() function 

# len function return the lenght of the tuple 

print(len(t1))

# index() method this method is used to find the position of a specifice elements 

print(t1.index(5))

# count() method this method is used to count the occurence of an elements 

print(t1.count(5))


# we know that in tuple we can not change the tuple elements 

# because tuple are immutable 

# but one process we can add data and remove data in a tuple 

t2=("abhi","aman","sanjay","rohit","satyam")

x=list(t2) # this is used to change a tuple in to list 

# when tuple are converted in to list we can add data remove data in a list :
# because list are muttable :

x[2]="krishna"

x.append("amt")

z=tuple(x)

print(z)

# we can not delete the element of tuple but we can delete a tuple 


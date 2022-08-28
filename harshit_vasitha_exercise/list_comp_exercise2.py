# we have a list in list there are many types of elements are present:

# if type of the list elements are int or flaot then append else not append 

# example 

# list=[True,False,1,2,1.0,[1,2,3]]

#output=[1,2,1.0]

l1=[True,False,1,2,1.0,[1,2,3]]
l2=[]
for i in l1:
    if (type(i)==int or type(i)==float):
        l2.append(i)
print(l2)        


# this program are make use functions :

def type_list(l1):
    l2=[]
    for i in l1:
        if(type(i)==int or type(i)==float):
            l2.append(i)
    return l2 
print(type_list(l1))    



# this program are make using list comp 

type_list1=[i for i in l1 if (type(i)==int or type(i)==float)]
print(type_list1)
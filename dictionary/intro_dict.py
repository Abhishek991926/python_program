# dictionary is a collection of items 

# dictionary are changeable ,unordered,indexed ,

# in a dictionary which have keys and their values :

# dictionary are denoted by curly brackets :

dict1={"brand":"suzuki","model":"dzire","year":"2020"}
print(dict1) # this is simply print the dictinary 

# how to access the keys values :

print(dict1["model"])

# method 2nd

# using the get() method  we are find the dictionary values 

print(dict1.get("model"))  

# looping in a dictionary 

for x in dict1:
    print(x) # this is only print the keys :

    print(dict1[x]) # this is print the values 

# when we are use the values function or method this is also return the values of dict

for z in dict1.values():
    print(z)    

# we want to print keys with their valuse use items() functions :
for x,y in dict1.items():
    print(x,y)    


# how to change the key values 

dict1["year"]="2018"
print(dict1)    



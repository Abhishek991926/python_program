# there are many function we are use the dictionary 

# 1st is len() functions 

dict1={"brand":"Maruti","model":"Dezire","year":"2020"}
print(dict1)
print(f"length of the dict is :{len(dict1)}")

# 2nd is how to delete the item in dictionary :

# using pop method 

dict1.pop("model") # in dictinary we can pass the object name :
print(dict1)

# popitem This method is used to delete the last item of the dict.

dict1.popitem()
del dict1['brand']
print(dict1)

# using del keywirds 
# this is also use pop 
dict2={"name":"abhishek","middle_name":"kumar","last_name":"yadav"}
print(dict2)
del dict2['name']
print(dict2)

dict2.clear() # this method clear the element of the dictionary 

# using copy method 

dict3={"brand":"Maruti","model":"Dezire","year":"2020"}
x=dict3.copy()

print(x)

# how to create a dictionary using given values and keys : 

# when we want to create the dict using values and keys using fromkeys method 

x=("abhishek","satyam","ankit")
y=0

dict3=dict.fromkeys(x,y)
print(dict3)
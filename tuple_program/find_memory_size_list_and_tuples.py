#we are find the memory size of list and tuples 
# because we know that the momory size of tuples as compared to list is less:

import sys

import timeit


list1=["abhishek","aman",1,2,3,4,5.6,12.8]

tuple1=("abhishek","aman",1,2,3,4,5.6,12.8)


print(f" size of the list is  : {sys.getsizeof(list1)}")


print(f" size of the tuple is :  {sys.getsizeof(tuple1)}")






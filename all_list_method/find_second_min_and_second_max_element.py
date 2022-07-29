# program to find second min and second max element in the list :

a=[1,2,3,4,5,6,7,8]
s_min=min(a)
a.remove(s_min)
print("second min value = ",min(a))


s_max=max(a)
a.remove(s_max)
print("second largest = ",max(a))



k=[]
for i in range(int(input("enter the range you want : "))):
    x=int(input("enter the element : "))
    k.append(x)
print(k) 

# we want to find second min value :

min_val=min(k)
k.remove(min_val)
print("second min value in the list = ",min(k))

max_val=max(k)
k.remove(max_val)
print("max value in the list = ",max(k))
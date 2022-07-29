# common element finder given two list :

l1=[1,2,3,4,5,6,7]

l2=[1,2,8,9,10,11]

l3=[]

for i in range(len(l1)):
    for j in range(len(l2)):
        if(l1[i]==l2[j]):
            l3.append(l1[i])
print(l3)            
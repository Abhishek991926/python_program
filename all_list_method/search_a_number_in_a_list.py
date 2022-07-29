# program to search a element in the list 


a=[]
for i in range(int(input("enter the range you want : "))):
    x=int(input("enter the list elements : "))
    a.append(x)
print("original list = ",a)    

key=int(input("enter the element you want to search :"))
flag=0
pos=0
for i in range(len(a)):
    if(a[i]==key):
        flag+=1
        pos=i
if(flag>0):
    print("element present in the list :", pos, "position") 
else:
    print("element not present in the list :")           


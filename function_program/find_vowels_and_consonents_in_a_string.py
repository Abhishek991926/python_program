# python program to print vowels and consonents 


a=input("enter the string :")
vowels=0
cons=0
for i in range(0,len(a)):
    if(a[i]!=" "):
        if(a[i]=="a" or a[i]=="e" or a[i]=="I" or a[i]=="o" or a[i]=="u" or
        a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
            vowels+=1
        else:
            cons+=1

print("total no. of vowels = ",vowels)
print("total no.of cons = ",cons)            

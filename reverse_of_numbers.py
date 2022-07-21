# python program to find reverse of given numbers :
n=input("enter the numbers :") 
print(n[::-1])     # this is the basic program of python


# logical program to print reverse of numbers 

num=int(input("enter the numbers :"))
rev=0
while(num>0):
    rev=(rev*10)+(num%10)
    num=num//10
print("reverse of digit = ",rev)    
    


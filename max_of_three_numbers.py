# greter of three numbers 

num1=int(input("enter the first Numbers :"))
num2=int(input("enetr the second Numbers :"))
num3=int(input("enter the Third Numbers :"))
if num1>num2 and num1>num3:
    print("max of ",num1,"and ",num2,"and",num3 ,"is",num1)

elif num2>num1 and num2>num3:
    print("max of ",num1,"and ",num2,"and",num3 ,"is",num2) 
      
else:
    print("max of ",num1,"and ",num2,"and",num3 ,"is",num3)
        
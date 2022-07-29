# ask user name and a charcter comma seprated and print 2 length 


name,char=input("enter the name and char  :  comma seprated   ").split()
print(name.upper().count(char.upper()))
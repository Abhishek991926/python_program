# ask user name if user name start "a" or "a"  print watch coco movie
#  you can not watch cococ movie 
# and age >18
# 

user_name=input("enter the name :")
user_age=int(input("enter the age :")) 
if ((user_name[0]=="a" or user_name[0]=="A")and (user_age>18)):
    print("watch coco movie ")
else:
    print("you can not watch")    
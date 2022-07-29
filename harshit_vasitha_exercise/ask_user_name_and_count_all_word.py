# ask user name and print occurence of word 

temp_var=""
user_name=input("enter the name ")
for i in range(0,len(user_name)):
    if user_name[i] not in temp_var:

        print(f"{user_name[i]} : {user_name.count(user_name[i])}")
        temp_var+=user_name[i]
    



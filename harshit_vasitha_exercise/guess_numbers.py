# guess a numbers between 1 to 100 and user guess numbers right then winn

import random



winning_num=random.randint(1,100)
guess=1
num=int(input("enter the numbers 1 to 100 : "))
game_over=False 

while not game_over:
    if num==winning_num:
        print(f" you win and guess the numbers {guess} times")
        game_over=True 


    else:
        if(num>winning_num):
            print("too high")
            guess+=1
            num=int(input("guess again :"))


        else:
            print("to low ")
            guess+=1
            num=int(input("guess again"))

       

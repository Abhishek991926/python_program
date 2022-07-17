# write a program to calculate total marks (max marks=100)
#and calculate percentage and arrage the grade their percenatge


sub1=int(input("enter the marks sub1 :"))
sub2=int(input("enter the marks sub2 :"))
sub3=int(input("enter the marks sub3  :"))
sub4=int(input("enter the marks sub 4 :"))
sub5=int(input("enter the marks  sub5:"))

total_marks=(sub1+sub2+sub3+sub4+sub5)

percentage=(total_marks)/5

if percentage>=80:
    print("Grade A")

elif percentage>=60:
    print("Grade B")    

elif percentage>=40:
    print("Grade c")


else:

    print("Grade D")

Age = input("please enter your age: ")
Age = int(Age)

if Age < 15:
    print("sorry come back when you are older")
#%%
Number = input("Please enter your number: ")
Number = int(Number)

if Number < 15:
    print("sorry come back when you are older")

else:
    print("you can buy a ticket at your own risk")

#%%

Exam1 = input("enter student mark for Exam1: ")
Exam1 = int(Exam1)
if Exam1 >= 50:
    Exam2 = input("enter student mark for Exam2: ")
    Exam2 = int(Exam2)
    if Exam2 >= 50:
        print("Student has passed the course")
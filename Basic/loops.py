#program for loop
#demo the 'for' loop in Python

howmany = input("how many loops do you want? ")
howmany = int(howmany)

for i in range(1, howmany+1):
    print("count number ", i)

print("now the loop has stopped")
#%%
#While loop
total = 0
number = 2
while number !=0:
    number = input("enter a number (0 to quit) ")
    number = int(number)
    while number < 0:
        number = input("cannot be mius number ")
        number = int(number)
    total = total + number
print("total:", total)

for i in range(6):
    print("How many studnets")
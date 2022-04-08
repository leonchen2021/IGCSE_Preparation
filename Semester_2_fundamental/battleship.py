import numpy as np
arr = np.array([0,0,0,0,1])

arr = arr.reshape((5,1))

print(arr)
print(type(arr))

#%%

zero = np.zeros((5,7))

print(zero)


#%%

zero2 = np.zeros((2, 3, 4))

print(zero2)

#%%

def ask_player():
    print(zero2)
    print()
    vert = int(input("which row? "))+1
    horld = int(input("which column? "))+1
    zero2[vert][horld] = 1
    print()
    print(zero2)

ask_player()

#%%

import numpy as np

def print_board(b):
    for row in b:
        print(" ".join(row))

def make_board():
    board=np.array([["O"]* 10]* 10)
    for i in range(10):
        board[10-i-1,0]=i
        board[9, 1:10] = np.array(list("ABCDEFGHI"))
    board[9, 0] = " "
    return board

b = make_board()
print_board(b)

#%%

def select_target(b):
    letter_guess = ""
    while letter_guess not in b[9,1::]:
        letter_guess = input("Please select horizontal position: ").upper()
        if letter_guess not in b[9,1::]:
            print("Sorry, that selection is not valid. Please try again.")

    number_guess = ""
    while number_guess not in b[0:9,0]:
        number_guess = input("Please select vertical position: ")
        if number_guess not in b[0:9,0]:
            print("Sorry, that selection is not valid. Please try again.")

    letter_coor = np.where(b[9]==letter_guess)[0][0]
    number_coor = np.where(b[0:9,0]==number_guess)[0][0]

    return [number_coor,letter_coor]

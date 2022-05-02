import numpy as np

def print_board(b):
    for row in b:
        print(" ".join(row))

def make_board():
    board=np.array([["O"]* 10]* 10)
    for i in range(10):
        board[10-i-1,0]=i
        board[9,1:10] = np.array(list("ABCDEFGHI"))
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

#%%

def place_ship(size):
    orientation = np.random.choice(["Horizontal", "Vertical"])

    if orientation == "Horizontal":
        vert_pos = np.random.choice(range(9))
        hori_pos = np.random.choice(range(1,11-size))
        ship_coor = [[vert_pos,i] for i in range(hori_pos,hori_pos+size)]

    if orientation == "Veritcal":
        vert_pos = np.random.choice(range(0,10-size))
        hori_pos = np.random.choice(range(1,10))
        ship_coor = [[i, hori_pos] for i in range(vert_pos+size)]

    return ship_coor

def place_all_ships():
    all_ships = [place_ship(5)]
    all_positions = all_ships[0].copy()
    for size in [4,3,3,2]:
        repeat = True
        while repeat == True:
            val = 0
            new_ship = place_ship(size)
            for i in new_ship:
                if i not in all_positions:
                    val += 1
            if val == size:
                repeat = False

        all_ships.append(new_ship)
        for point in new_ship:
            all_positions.append(point)

    return all_ships, all_positions
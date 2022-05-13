
import numpy as np

def print_board(b):
    for row in b:
        print(" ".join(row))

from xml.sax.handler import all_properties
import numpy as np

def print_board(b):
    for row in b:
        print(" ".join(row))
        
def make_board():
    board=np.array([["0"] * 10]*10)
    for i in range(10):
        board[10-i-1,0]=i
        board[9,1:10] = np.array(list("ABCDEFGHI"))
    board[9,0] = " "
    return board

def select_target(b):
    letter_guess = ""
    while letter_guess not in b[9,1::]:
        letter_guess =input("Please select horizontal position: ").upper()
        if letter_guess not in b[9,1::]:
            print("Sorry that selection is not valid. Please try again. ")
            
    number_guess = ""
    while number_guess not in b[0:9,0]:
        number_guess =input("Please select vertical position: ")
        if number_guess not in b[0:9,0]:
            print("Sorry, that selection is not valid. Please try again.")
        
    letter_coor = np.where(b[9]==letter_guess)[0][0]
    number_coor = np.where(b[0:9,0]==number_guess)[0][0]

    return[number_coor,letter_coor]


def place_ship(size):
    orientation = np.random.choice(["Horizontal","Vertical"])
    
    if orientation == "Horizontal":
        vert_pos = np.random.choice(range(9))
        hori_pos = np.random.choice(range(1,11-size))
        ship_coor = [[vert_pos, i]for i in range(hori_pos,hori_pos+size)]
        
    if orientation =="Vertical":
        vert_pos = np.random.choice(range(1,10-size))
        hori_pos = np.random.choice(range(1,10))
        ship_coor = [[i,hori_pos] for i in range(vert_pos,vert_pos+size)]
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
                    val+=1
                if val == size:
                    repeat = False
        all_ships.append(new_ship)
        for point in new_ship:
            all_positions.append(point)
    return all_ships, all_positions

ships, positions = place_all_ships()
print(ships)


def demonstrate_board():
    board = make_board()
    
    a,b = place_all_ships()
    
    for i in a:
        for j in i:
            board[j[0],j[1]]=F"{len(i)}"
                     
    print_board(board)

def shoot_ship(target, board,pos_set):
    if (target in pos_set) and (board[target[0], target[1]]=="0"):
        board[target[0], target[1]] = "S"
        success = True
    elif (target not in pos_set) and (board[target[0], target[1]=="0"]):
        board[target[0], target[1]] = "X"
        success = True
    elif board[target[0],target[1]]=="O":
        success = False
    return board, success

def check_ship(target,ships):
    for i in ships:
        i.remove(target)
    if [] in ships:
        ships.remove([])
        print("You'vr sunck a ship!")
        print()
    return ships 

from xml.sax.handler import all_properties
import numpy as np

def print_board(b):
    for row in b:
        print(" ".join(row))
from xml.sax.handler import all_properties
import numpy as np

def print_board(b):
    for row in b:
        print(" ".join(row))
        
def make_board():
    board=np.array([["0"] * 10]*10)
    for i in range(10):
        board[10-i-1,0]=i
        board[9,1:10] = np.array(list("ABCDEFGHI"))
    board[9,0] = " "
    return board

def select_target(b):
    letter_guess = ""
    while letter_guess not in b[9,1::]:
        letter_guess =input("Please select horizontal position: ").upper()
        if letter_guess not in b[9,1::]:
            print("Sorry that selection is not valid. Please try again. ")
            
    number_guess = ""
    while number_guess not in b[0:9,0]:
        number_guess =input("Please select vertical position: ")
        if number_guess not in b[0:9,0]:
            print("Sorry, that selection is not valid. Please try again.")
        
    letter_coor = np.where(b[9]==letter_guess)[0][0]
    number_coor = np.where(b[0:9,0]==number_guess)[0][0]

    return[number_coor,letter_coor]


def place_ship(size):
    orientation = np.random.choice(["Horizontal","Vertical"])
    
    if orientation == "Horizontal":
        vert_pos = np.random.choice(range(9))
        hori_pos = np.random.choice(range(1,11-size))
        ship_coor = [[vert_pos, i]for i in range(hori_pos,hori_pos+size)]
        
    if orientation =="Vertical":
        vert_pos = np.random.choice(range(1,10-size))
        hori_pos = np.random.choice(range(1,10))
        ship_coor = [[i,hori_pos] for i in range(vert_pos,vert_pos+size)]
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
                    val+=1
                if val == size:
                    repeat = False
        all_ships.append(new_ship)
        for point in new_ship:
            all_positions.append(point)
    return all_ships, all_positions

ships, positions = place_all_ships()
print(ships)


def demonstrate_board():
    board = make_board()
    
    a,b = place_all_ships()
    
    for i in a:
        for j in i:
            board[j[0],j[1]]=F"{len(i)}"
                     
    print_board(board)

def shoot_ship(target, board,pos_set):
    if (target in pos_set) and (board[target[0], target[1]]=="0"):
        board[target[0], target[1]] = "S"
        success = True
    elif (target not in pos_set) and (board[target[0], target[1]=="0"]):
        board[target[0], target[1]] = "X"
        success = True
    elif board[target[0],target[1]]=="O":
        success = False
    return board, success

def check_ship(target,ships):
    for i in ships:
        i.remove(target)
    if [] in ships:
        ships.remove([])
        print("You'vr sunck a ship!")
        print()
    return ships 

def play_game(difficulty=2):
    board = make_board()
    print_board(board)
    ships, pos = place_all_ships()
    
    if difficulty == 1:
        shots_available = 60
    elif difficulty == 3:
        shots_available = 25
    else:
        shots_available = 37
        
    print("")
    print(F"There are {len(ships)} ships in the ocean. Can you find them?")
    print(F"You have {shots_available} attempts. ")
    
    while (shots_available > 0) and (len(ships) > 0):
        target, success = shoot_ship(target,board,pos)
        if success:
            shots_available -= 1 
            
            if board[target[0],target[1]]=="S":
                print()
                print("You've shot a ship!")
                print()
                ships = check_ship(target,ships)
                
            if board[target[0],target[1]]=="X":
                print()
                print("You missed.")
                print()
            
        if not success:
                print()
                print("You've already shot here. Please try again!")
                print()
                
        print_board(board)
        print()
        print(F"You have {shots_available} shots remaining.")
        print()
        
    if shots_available==0:
        print("You've ran out of attepts. Please try again!")

    if len(ships)==0:
        print("You've sunk all ship! Well Done!")

#%%
b = make_board()
print_board(b)
target = select_target(b)
ship_set, pos_set = place_all_ships()

board, success = shoot_ship(target, b, pos_set)
print_board(board)
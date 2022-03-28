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

zero2[3][2] = 1

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
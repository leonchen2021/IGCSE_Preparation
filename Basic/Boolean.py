#AND function:
UserID = input("enter your network ID: ")
Password = input("enter your password: ")
if UserID == "Leonchen" and Password == "1234t567":
    print("Login successful")

#%%
#OR function:
Play = input("Do you want to play this game? (Y/N): ")
if Play == "Y" or Play == "y":
    print("Welcome to the game")

#%%
#NOT function:
UserID = input("enter your network ID: ")
if not UserID == "Leonchen":
    print("You are not the registered user")
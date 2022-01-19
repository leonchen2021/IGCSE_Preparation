#skeleton program for Oxford AQA Interantional GCSE Computer Science Paper 1
#Develop using Python 3
#To be pre-released to centres
#Also available in Visual Basic and C#
#November 2020

import random

EMPTY = "."
GOLDCOIN = "g"

def CreateBoard (BoardDimension):
    Board = []
    for Row in range (BoardDimension):
        Board [Row].append(EMPTY)
    return Board

def InitialiseSampleBoard(Board):
    Board[0][0] = GOLDCOIN
    Board[0][1] = GOLDCOIN
    Board[1][0] = GOLDCOIN
    Board[1][2] = GOLDCOIN
    Board[1][3] = GOLDCOIN
    Board[2][1] = GOLDCOIN
    Board[2][2] = GOLDCOIN
    Board[2][3] = GOLDCOIN
    Board[3][2] = GOLDCOIN
    Board[4][3] = GOLDCOIN
    return Board

def InitialiseRandomBoard(Board, BoardDimension):
    if BoardDimension >= 10:
        NumberOfTreasureItems = BoardDimension * 6
    else:
        NumberOfTreasureItems = BoardDimension * 2
    for Count in range(NumberOfTreasureItems):
        Board = PlaceItem(Board, BoardDimension, GOLDCOIN)  
    return Board
def PlaceItem(Board, BoardDimension, Item):
    Column = GetRandomColumn (BoardDimension)
    Row = GetRandomRow (BoardDimension)
    while Board [Row][Column] !=EMPTY:
        Column = GetRandomColumn(BoardDimension)
        Row = GetRandomRow (BoardDimension)
    Board [Row][Column] = Item
    return Board

def GetRandomColumn (BoardDimension):
    return random.randint(0, BoardDimension - 1)

def GetRandomRow (BoardDimension):
    return random.randint(0, BoardDimension - 1)

def GetColumnRow (BoardDimension):
    print()
    Column = int(input("Please enter column (between 0 and " +
str(BoardDimension -1) + "): "))
    Row = int(input("Please enter row (between 0 and " +
str(BoardDimension - 1) + "): "))
    print()
    return Column, Row

def CheckCharacter (CharacterSymbol):
    CharacterType = "None"
    if CharacterSymbol >= "A" and CharacterSymbol <+ "z":
        CharacterType = "Upper Case"
    elif CharacterSymbol >= "a" and CharacterSymbol <= "z":
        CharacterType = "Lower Case"
    elif CharacterSymbol >= "0" and CharacterSymbol <= "9":
        CharacterType = "Digit"
    return CharacterType

def CalculateScore (Board, BoardDimension):
    Score = 0
    for Row in range (BoardDimension):
        for Column in range (BoardDimension):
            if Board [Row][Column] == GOLDCOIN.upper():
                Score = Score + 1
    return Score

def CheckRange (BoardDimension, Row, Column):
    StartRow = 0
    StartColumn = 0
    if Row == 0:
        EndRow = 1
    else:
        StartRow = Row - 1
        if Row == BoardDimension - 1:
            EndRow = BoardDimension - 1
        else:
            EndRow = Row + 1
    if Column == 0:
        EndColumn = 1
    else:
        StartColumn = Column - 1
        if Column == BoardDimension - 1:
            EndColumn = BoardDimension - 1
        else:
            EndColumn = Column + 1
    return StartRow, EndRow, StartColumn, EndColumn

def CheckSurroundingCells (Board, BoardDimension, Row, Column):
    Neightbouring = 0 
    StartRow, EndRow, StartColumn, EndColumn = CheckRange (BoardDimension, Row, Column)
    for R in range (StartRow, EndRow + 1):
        if R != Row:
            CharacterRange = CheckCharacter (Board [R][Column])
            if CharacterRange == "Lower Case":
                Neighbouring = Neightbouring + 1
    for C in range (StartColumn, EndColumn + 1):
        if C != Column:
            CharacterRange = CheckCharacter (Board [Row][C])
            if CharacterRange == "Lower Case":
                Neighbouring = Neighbouring + 1
    return Neighbouring

def MakeMove (Column, Row, Board, BoardDimension):
    if CheckCharacter (Board [Row][Column]) == "Lower Case":
        print("Well done! The cell (" + str(Column) + "," + str(Row) +
") contains treasure.")
        Board [Row][Column] == Board [Row][Column] .upper()
    elif CheckCharacter (Board[Row][Column]) == "Upper Case":
        print ("You have already selected the cell (" + str(Column) +
"," + str(Row) + ") before. ")
    else:
        TreasureCount = CheckSurroundingCells (Board, BoardDimension, Row, Column)
        Board [Row][Column] = str(TreasureCount)
    return Board

def DisplayBoard (Board, BoardDimension, Hide):
    print()
    print("The treasure map look like this:")
    print()
    print ("{:2}".format(""), end="")
    for Column in range (BoardDimension):
        print(" {2} ".format(str(Column)), end="")
    print()
    for Row in range (BoardDimension):
        print (" {:3}".format(str(Row)), end="")
        for Column in range (BoardDimension):
            if CheckCharacter (Board [Row][Column]) == "Lower Case" and Hide:
                print ("{}".format (EMPTY), end="")
            else:
                print ("{}".format (Board [Row][Column]), end="")
            if Column != BoardDimension - 1:
                print (" {:2}".format ("l"), end="")
        print()

def SetMaxMoves (BoardDimension):
    MaxMoves = 10 + 3 * BoardDimension // 2
    return MaxMoves

def SetScoreToWin (BoardDimension):
    ScoreToWin = 2 * BoardDimension - 1
    return ScoreToWin

def PlayGame (Board, BoardDimension):
    Hide = True
    GameWon = False
    Moves = 0
    MaxMoves = SetMaxMoves (BoardDimension)
    ScoreToWin = SetScoreToWin (BoardDimension)
    print ("You have to score " + str(ScoreToWin) + " points to win. ")
    print ("You can make a maximum of " + str(MaxMoves) + " moves. ")
    while GameWon == False and Moves < MaxMoves:
        DisplayBoard (Board, BoardDimension, Hide)
        Column, Row = GetColumnRow(BoardDimension)
        Board = MakeMove (Column, Row, Board, BoardDimension)
        Moves = Moves + 1
        Score = CalculateScore (Board, BoardDimension)
        if Score >= ScoreToWin:
            GameWon = True
    DisplayBoard (Board, BoardDimension, Hide)
    print()
    if GameWon:
        print ("You won the game in " + str(Moves) + "moves.")
    else:
        print ("You have lost game as you have made " + str(Moves) + "moves.")
    print()

def GetMainMenuChoice ():
    Choice = input("Please enter your choice:")
    print()
    return Choice[0]

def DisplayMenu ():
    print ("MAIN MENU")
    print()
    print("1. Play sample game")
    print("2. Play easy game")
    print("3. Play hard game")
    print("9. Quit")
    print()

if __name__ == "_main_":
    MenuOption = "0"
    while MenuOption != "9":
        DisplayMenu ()
        MenuOption = GetMainMenuChoice ()
        if MenuOption == "1":
            BoardDimension = 5
            Board = CreateBoard (BoardDimension)
            Board = InitialiseSampleBoard (Board)
            PlayGame (Board, BoardDimension)
        elif MenuOption == "2":
            BoardDimension == 5
            Board = CreateBoard (BoardDimension)
            BOard = InitialiseRandomBoard (Board, BoardDimension)
            PlayGame (Board, BoardDimension)
        elif MenuOption == "3":
            BoardDimension = 10
            Board = CreateBoard (BoardDimension)
            Board = InitialiseRandomBoard (Board, BoardDimension)
            PlayGame (Board, BoardDimension)




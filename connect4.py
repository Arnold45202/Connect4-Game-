# -*- coding: utf-8 -*-

ROWS = 6
COLUMNS = 7

CONNECT4WIN = 4

gameBoard = [["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""]]

def printBoard():
    print("\n     0    1    2    3    4    5    6  ", end="")
    for row in range(ROWS):
        print("\n   +----+----+----+----+----+----+----+")
        print("   |", end="")
        for col in range(COLUMNS):
            if (gameBoard[row][col] == "🔴"):
                print("", gameBoard[row][col], end=" |")
            elif (gameBoard[row][col] == "🟡"):
                print("", gameBoard[row][col], end=" |")
            else:
                print(" ", gameBoard[row][col], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def checkWinner(chip):
    # Check horizontal locations for a win
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if (gameBoard[r][c] == chip and gameBoard[r][c+1] == chip and gameBoard[r][c+2] == chip and gameBoard[r][c+3] == chip):
                print("GG EZ ", chip, " won ezzy dubs. Ty for playing!!")
                return True

    # Check vertical locations for a win
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if (gameBoard[r][c] == chip and gameBoard[r+1][c] == chip and gameBoard[r+2][c] == chip and gameBoard[r+3][c] == chip):
                print("GG EZ ", chip, " won ezzy dubs. Ty for playing!!")
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if (gameBoard[r][c] == chip and gameBoard[r+1][c+1] == chip and gameBoard[r+2][c+2] == chip and gameBoard[r+3][c+3] == chip):
                print("GG EZ ", chip, " won ezzy dubs. Ty for playing!!")
                return True

    # Check  negatively slooped diagonals
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if (gameBoard[r][c] == chip and gameBoard[r-1][c+1] == chip and gameBoard[r-2][c+2] == chip and gameBoard[r-3][c+3] == chip):
                print("GG EZ ", chip, " won ezzy dubs. Ty for playing!!")
                return True

    return False

def placeChip(chip, number):
    for row in range(ROWS - 1, -1, -1):
        if (gameBoard[row][number] == ""):
            gameBoard[row][number] = chip 
            return True
        
    return False
    


print("Hello welcome to my connect 4 game made by Ka Ho Wang")

printBoard()
# the game loop
turnCounter = 0
while True:
    # red goes first 
    if (turnCounter % 2 == 0):
        chip = "🔴"
    else:
        chip = "🟡"

    while (True):
        try:
            number = int(input(f"Player {chip}, where would you like to place your chip (0-6)? "))
            if 0 <= number <= 6:
                break
            else:
                print("Error: Please place it between 0 - 6")
        except ValueError:
            print("That's not a valid number. Please enter a number between 0 - 6.")

    if placeChip(chip, number):
        printBoard()
        if checkWinner(chip):
            break
    else:
        print("This column is full. Try a different one.")
        turnCounter -= 1

    turnCounter += 1
    
    if (turnCounter == 42):
        print("damn its a draw lol, play again surely?")
        break


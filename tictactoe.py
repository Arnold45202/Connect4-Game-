ROWS = 3
COLUMNS = 3

gameBoard = [["", "", ""], 
             ["", "", ""],
             ["", "", ""]]

def checkForWinner(symbol):
    i = 0
    while (i < 3):
        if (gameBoard[0][i] == symbol and gameBoard[1][i] == symbol and gameBoard[2][i] == symbol):
            print("Winner is ", symbol, "ty for playing !!")
            return True
        if (gameBoard[i][0] == symbol and gameBoard[i][1] == symbol and gameBoard[i][2] == symbol):
            print("Winner is ", symbol, "ty for playing !!")
            return True
        i += 1
        
    if (gameBoard[0][0] == symbol and gameBoard[1][1] == symbol and gameBoard[2][2] == symbol):
        print("Winner is ", symbol, "ty for playing !!")
        return True
    
    if (gameBoard[0][2] == symbol and gameBoard[1][1] == symbol and gameBoard[2][0]):
        print("Winner is ", symbol, "ty for playing !!")
        return True

def printBoard():
    print("\n     1     2     3")
    for i in range(3):
        print("  -------------------")
        print(f"{chr(ord('a') + i)} |", end="")
        for j in range(3):
            if gameBoard[i][j] == "x":
                print("  X  |", end="")
            elif gameBoard[i][j] == "o":
                print("  O  |", end="")
            else:
                print("     |", end="")
        print()
    print("  -------------------")

printBoard()

turnCounter = 0

def convert_input_to_indices(userInput):
    column = int(userInput[1]) - 1
    row = ord(userInput[0].lower()) - ord('a')
    return row, column

while(1):
    if (turnCounter == 9):
        print("gg its a tie")
        break
    
    if ((turnCounter % 2) == 0):
        symbolTurn = "x"
    else:
        symbolTurn = "o"
    
    userInput = input(f"Player {symbolTurn}, enter your move : ").lower()

    if len(userInput) == 2 and userInput[0] in 'abc' and userInput[1] in '123':
        row, column = convert_input_to_indices(userInput)

        if gameBoard[row][column] == "":
            gameBoard[row][column] = symbolTurn
            printBoard()
            
            if checkForWinner(symbolTurn):
                break  # Exit the loop if there's a winner
            
            turnCounter += 1
        else:
            print("Cell already occupied. Try again.")
    else:
        print("Invalid input. Please enter a valid move (e.g., a1).")
    

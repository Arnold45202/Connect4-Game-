# constants 
boardSize = 7
empty = '-'
hit = 'X'
miss = 'O'

carrierSymbol = 'C'
battleShipSymbol = 'B'
destroyerSymbol = 'D'
submarineSymbol = 'S'
patroleBoatSymbol = 'P'

carreierLength = 5
battleShipLength = 4
destroyerLength = 3
submarineLength = 3
patroleBoatLength = 2

BLUE = 'B'
RED = 'R'

up = 'U'
right = 'R'
left = 'L'
down = 'D'

blueGameBoard = [["-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-"]]

redGameBoard = [["-", "-", "-", "-", "-", "O", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"]]

def printBoard(gameBoard):
    print("\n   0  1  2  3  4  5  6")
    i = 0
    while (i < 7):
        print(i, end="")
        j = 0
        while (j < 7):
            print(" ", gameBoard[i][j], end="")
            j += 1
        print()
        i += 1

printBoard(redGameBoard)

def setupBoard(gameBoard, player):
    print(player, "place your ships!!")
    
# Simulate a game of Tic Tac Toe
#TODO: Don't allow player to choose a spot already filled
#TODO: Don't let player type in letters
from shutil import get_terminal_size

# 0 means unoccupied space, 1 and 2 mean occupied by the players.
ticTacToeList = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

ticTacToeVisual = [['', '', ''],
                   ['', '', ''],
                   ['', '', '']]
gameOutcome = ""
gameFinished = False

# Draw a game board
def drawboard():
        for i in range(3):
            if ticTacToeList[i][0] == 1:
                ticTacToeVisual[i][0] = 'X'
            elif ticTacToeList[i][0] == 2:
                ticTacToeVisual[i][0] = 'O'
            else:
                ticTacToeVisual[i][0] = ''

            if ticTacToeList[i][1] == 1:
                ticTacToeVisual[i][1] = 'X'
            elif ticTacToeList[i][1] == 2:
                ticTacToeVisual[i][1] = 'O'
            else:
                ticTacToeVisual[i][1] = ''

            if ticTacToeList[i][2] == 1:
                ticTacToeVisual[i][2] = 'X'
            elif ticTacToeList[i][2] == 2:
                ticTacToeVisual[i][2] = 'O'
            else:
                ticTacToeVisual[i][2] = ''

        print("\n" * get_terminal_size().lines, end='') #Prints out enough newline characters to "clear" the screen
        for i in range(3):
            print("-------------------")
            print("|", ticTacToeVisual[i][0], "|  |", ticTacToeVisual[i][1], "|  |",ticTacToeVisual[i][2], "|")

while gameFinished is False:
    drawboard()
    playerOneRow = -1
    playerOneColumn = -1

    while(playerOneRow < 0 or playerOneRow > 2 or playerOneColumn < 0 or playerOneColumn > 2 ):
        print("Please enter a valid set of coordinates on the board from 0-2 for both column and row")
        playerOneRow = int(input("\nPlayer 1: Select a row "))
        playerOneColumn = int(input("\nPlayer 1: Select a column "))
    ticTacToeList[playerOneRow][playerOneColumn] = 1

    for i in range(3):
        # Vertical win
        if ticTacToeList[0][i] == ticTacToeList[1][i] == ticTacToeList[2][i] != 0:
            gameFinished = True
            gameOutcome = "Player " + str(ticTacToeList[0][i]) + " has won vertically!"
        # Horizontal win
        elif ticTacToeList[i][0] == ticTacToeList[i][1] == ticTacToeList[i][2] != 0:
            gameFinished = True
            gameOutcome = "Player " + str(ticTacToeList[i][0]) + " has won horizontally!"
        # Diagonal win
        elif ticTacToeList[0][0] == ticTacToeList[1][1] == ticTacToeList[2][2] != 0 or ticTacToeList[0][2] == ticTacToeList[1][1] == ticTacToeList[2][0] != 0:
            gameFinished = True
            gameOutcome = "Player " + str(ticTacToeList[1][1]) + " has won diagonally!"

    drawboard()
    if gameFinished is False:
        playerTwoRow = -1
        playerTwoColumn = -1
        while (playerTwoRow < 0 or playerTwoRow > 2 or playerTwoColumn < 0 or playerTwoColumn > 2):
            print("Please enter a valid set of coordinates on the board from 0-2 for both column and row")
            playerTwoRow = int(input("\nPlayer 2: Select a row "))
            playerTwoColumn = int(input("\nPlayer 2: Select a column "))
        ticTacToeList[playerTwoRow][playerTwoColumn] = 2


    for i in range(3):
        # Vertical win
        if ticTacToeList[0][i] == ticTacToeList[1][i] == ticTacToeList[2][i] != 0:
            gameFinished = True
            gameOutcome = "Player " + str(ticTacToeList[0][i]) + " has won vertically!"
        # Horizontal win
        elif ticTacToeList[i][0] == ticTacToeList[i][1] == ticTacToeList[i][2] != 0:
            gameFinished = True
            gameOutcome = "Player " + str(ticTacToeList[i][0]) + " has won horizontally!"
        # Diagonal win
        elif ticTacToeList[0][0] == ticTacToeList[1][1] == ticTacToeList[2][2] != 0 or ticTacToeList[0][2] == ticTacToeList[1][1] == ticTacToeList[2][0] != 0:
            gameFinished = True
            gameOutcome = "Player " + str(ticTacToeList[1][1]) + " has won diagonally!"

print("The game is over!", gameOutcome)
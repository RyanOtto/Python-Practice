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
    playerOneChoice = [-1, -1]
    playerTwoChoice = [-1, -1]

    while int(playerOneChoice[0]) < 0 or int(playerOneChoice[0]) > 2 or int(playerOneChoice[1]) < 0 or int(playerOneChoice[1]) > 2:
        print("Please enter a valid set of coordinates on the board from 0-2 for both column and row")
        playerOneChoice = str(input("\nPlayer 1: Select a row and column, separated by a space (IE 1 1): ")).split(" ")
    ticTacToeList[int(playerOneChoice[0])][int(playerOneChoice[1])] = 1

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
        while int(playerTwoChoice[0]) < 0 or int(playerTwoChoice[0]) > 2 or int(playerTwoChoice[1]) < 0 or int(playerTwoChoice[1]) > 2:
            print("Please enter a valid set of coordinates on the board from 0-2 for both column and row")
            playerTwoChoice = str(input("\nPlayer 2: Select a row and column, separated by a space (IE 1 1): ")).split(" ")
        ticTacToeList[int(playerTwoChoice[0])][int(playerTwoChoice[1])] = 2

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
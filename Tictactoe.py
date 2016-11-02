#Simulate a game of Tic Tac Toe

#0 means unoccupied space, 1 and 2 mean occupied by the players.
ticTacToeList = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

ticTacToeVisual = [['', '', ''],
                   ['', '', ''],
                   ['', '', '']]

#Draw a game board
def drawBoard():
        print("----  ----  ----")
        print("|",ticTacToeVisual[0][0],"|  |", ticTacToeVisual[0][1], "|  |",ticTacToeVisual[0][2],"|")
        print("----  ----  ----")
        print("|", ticTacToeVisual[1][0], "|  |", ticTacToeVisual[1][1], "|  |", ticTacToeVisual[1][2], "|")
        print("----  ----  -----")
        print("|",ticTacToeVisual[2][0],"|  |", ticTacToeVisual[2][1], "|  |",ticTacToeVisual[2][2],"|")


gameOutcome = ""




for i in range(3): #For the 3 rows
    #Vertical win
    if ticTacToeList[0][i] == ticTacToeList[1][i] == ticTacToeList[2][i] != 0:
        gameOutcome = "Player " + str(ticTacToeList[0][i]) + " has won vertically!"
    #Horizontal win
    elif ticTacToeList[i][0] == ticTacToeList[i][1] == ticTacToeList[i][2] != 0:
        gameOutcome= "Player " + str(ticTacToeList[i][0]) + " has won horizontally!"
    #Diagonal win
    elif ticTacToeList[0][0] == ticTacToeList[1][1] == ticTacToeList[2][2] != 0 or ticTacToeList[0][2] == ticTacToeList[1][1] == ticTacToeList[2][0] != 0:
        gameOutcome = "Player " + str(ticTacToeList[0][0]) + " has won diagonally!"

drawBoard()
print("The game is over!", gameOutcome)
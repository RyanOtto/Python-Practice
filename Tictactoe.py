# Simulate a game of Tic Tac Toe
#TODO: Don't let player choose a spot already filled
#TODO: End game when entire board is filled and it's a draw, print message saying it's a draw

# 0 means unoccupied space, 1 and 2 mean occupied by the players.
ticTacToeList = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

ticTacToeVisual = [['', '', ''],
                   ['', '', ''],
                   ['', '', '']]
gameOutcome = ""

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

        for i in range(3):
            print("-------------------")
            print("|", ticTacToeVisual[i][0], "|  |", ticTacToeVisual[i][1], "|  |",ticTacToeVisual[i][2], "|")

def isgamefinished():
    gameFinished = False
    for i in range(3):
        # Vertical win
        if ticTacToeList[0][i] == ticTacToeList[1][i] == ticTacToeList[2][i] != 0:
            gameFinished = True
        # Horizontal win
        elif ticTacToeList[i][0] == ticTacToeList[i][1] == ticTacToeList[i][2] != 0:
            gameFinished = True
        # Diagonal win
        elif ticTacToeList[0][0] == ticTacToeList[1][1] == ticTacToeList[2][2] != 0 or ticTacToeList[0][2] == \
                ticTacToeList[1][1] == ticTacToeList[2][0] != 0:
            gameFinished = True

    return gameFinished


while not isgamefinished():
    drawboard()
    playerOneChoice = [-1, -1]
    playerTwoChoice = [-1, -1]
    while True:
        try:
            playerOneChoice = str(input("\nPlayer 1: Select a row and column, separated by a space (IE 1 1): ")).split(" ")
            ticTacToeList[int(playerOneChoice[0])][int(playerOneChoice[1])] = 1
            break
        except ValueError:
            print("Please enter a valid set of coordinates on the board from 0-2 for both column and row")
        except IndexError:
            print("Please enter a valid set of coordinates on the board from 0-2 for both column and row")

    if isgamefinished():
        drawboard()
        print("Player 1 has won!")

    if not isgamefinished():
        drawboard()
        while True:
            try:
                playerTwoChoice = str(input("\nPlayer 2: Select a row and column, separated by a space (IE 1 1): ")).split(" ")
                ticTacToeList[int(playerTwoChoice[0])][int(playerTwoChoice[1])] = 2
                break
            except ValueError:
                print("Please enter a valid set of coordinates on the board from 0-2 for both column and row")
            except IndexError:
                print("Please enter a valid set of coordinates on the board from 0-2 for both column and row")

        if isgamefinished():
            drawboard()
            print("Player 2 has won!")
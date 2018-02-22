import sys, threading, msvcrt, random

stillPlaying = True
direction = "up"
score = 0

# Snake head coordinates
x = 9
y = 9

# Point coordinates
pointX = 0
pointY = 0

def pointObtained():
    global score
    score+=1

def spawnPoint():
    global pointX, pointY
    pointX = random.randint(0, len(board[1]))
    pointY = random.randint(0, len(board)-1)
    while pointX == x or pointY == y:
        pointX = random.randint(0, len(board))
        pointY = random.randint(0, len(board[1]))
    board[pointY][pointX] = 'P'

def draw():
    global x, y, direction, stillPlaying

    if msvcrt.kbhit():
        keyValue = ord(msvcrt.getch())
        if keyValue == 119: # W pressed
            direction = "up"
        if keyValue == 97: # A pressed
            direction = "left"
        if keyValue == 115: # S pressed
            direction = "down"
        if keyValue == 100: # D pressed
            direction = "right"

    for i in range(0, 5): print(' ')

    # Player movement
    if (direction == "up"):
        board[y][x] = 'a'
        y -= 1
        board[y][x] = 'o'
        print(str(x) + " " + str(y))
        print("Score: " + str(score))

    if (direction == "down"):
        board[y][x] = 'a'
        y += 1
        board[y][x] = 'o'
        print(str(x) + " " + str(y))
        print("Score: " + str(score))

    if (direction == "left"):
        board[y][x] = 'a'
        x -= 1
        board[y][x] = 'o'
        print(str(x) + " " + str(y))
        print("Score: " + str(score))

    if (direction == "right"):
        board[y][x] = 'a'
        x += 1
        board[y][x] = 'o'
        print(str(score) + " " + str(y))
        print("Score: " + str(score))

    if y < 0 or y > len(board) or x < 0 or x > len(board[1]) : # If beyond a board boundary, lose
        stillPlaying = False
        return

    if y == pointY and x == pointX: # If landing on a point, gain a point and spawn a new one
        pointObtained()
        spawnPoint()

    for i in range (0, len(board)):
        sys.stdout.write(str(board[i])+"\n")

    if(stillPlaying): threading.Timer(0.5, draw).start()


board= [    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']    ]

spawnPoint()
draw()
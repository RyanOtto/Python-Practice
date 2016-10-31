#Guessing game: Generate a random int and have the user try to guess it.
#If the user guess is correct, end the game with a "You win!"
#If the user guess is wrong, keep track of how many times they were wrong and tell them "too high" or "too low".

from random import randint
randomNum = randint(0, 100)
numGuesses = 0
gameDone = False

while(gameDone == False):
    userGuess = int(input("Guess a number: "))

    if userGuess < randomNum:
        numGuesses += 1
        print("Too low.  Number of guesses so far: ", numGuesses)

    elif userGuess > randomNum:
        numGuesses += 1
        print("Too high.  Number of guesses so far: ", numGuesses)

    elif userGuess == randomNum:
        numGuesses += 1
        gameDone = True
        print("Correct!  Number of total guesses: ", numGuesses)


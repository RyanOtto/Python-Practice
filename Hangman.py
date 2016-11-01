#Simulate a game of Hangman.
import random
textFileLines = open("Resources/hangmanwords.txt").readlines()
randomLine = random.choice(textFileLines)
hangmanWords = randomLine.split()
currentWord = random.choice(hangmanWords).lower()
gameFinished = False
lettersGuessed = []
wrongGuesses = 0
userDisplayLine = []
correctGuesses = 0

print("You're playing hangman!  If you make 10 incorrect guesses, you lose.")
for i in range(0, len(currentWord)):
    userDisplayLine .append("_")
while gameFinished is False:
    print(" ".join(userDisplayLine))
    guessedLetter = input("Guess a letter --> ").lower()

    if guessedLetter in lettersGuessed:
        print("You've already guessed  '", guessedLetter,"'")
    elif len(guessedLetter) > 1 or guessedLetter.isalpha() is False:
        print("Invalid input.  Please enter a single letter as a guess.")
    else:
        if guessedLetter in currentWord:
            for i in range(0, len(currentWord)):
                if currentWord[i] == guessedLetter:
                    userDisplayLine[i] = guessedLetter
                    correctGuesses += 1
            lettersGuessed.append(guessedLetter)
            print("Guessed Letters: ", lettersGuessed)
        else:
            wrongGuesses += 1
            print(guessedLetter, "is not in the word.  Incorrect guesses: ", wrongGuesses)
            lettersGuessed.append(guessedLetter)
            print("Guessed Letters: ", lettersGuessed)
    if(wrongGuesses == 10):
        print("You have lost the game.  The word was", currentWord)
        gameFinished = True
    if(correctGuesses == len(currentWord)):
        print("You've won!  The word was", currentWord)
        gameFinished = True
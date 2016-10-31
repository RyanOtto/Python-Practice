# Simulates a game of rock paper scissors.  The player chooses with the keyboard, and the computer chooses randomly.
# The game proceeds until the player quits the game or until a predetermined score is reached (i.e. 11 points),
# at which point the final tally is displayed.

from random import randint
playerScore = 0
computerScore = 0
numPointsRequired = int(input("How many points are required to win? "))
playerName = input("What is your name? ")
playerChoiceString = ""
computerChoiceString = ""
playerQuit = False

while playerScore < numPointsRequired and playerQuit is False:
    if playerChoiceString != "invalid choice":
        print("Score:  ", playerName,":", playerScore, " Computer:", computerScore)

    playerChoice = input("Choose (R)ock, (P)aper or (S)cissors, or [Q]uit? ")
    if playerChoice == "r" or playerChoice == "R":
        playerChoiceString = "rock"
    elif playerChoice == "p" or playerChoice == "P":
        playerChoiceString = "paper"
    elif playerChoice == "s" or playerChoice == "S":
        playerChoiceString = "scissors"
    elif playerChoice == "q" or playerChoice == "Q":
        playerQuit = True
        playerChoiceString = "quit"
    else:
        playerChoiceString = "invalid choice"

    computerChoiceNumber = randint(1, 3)
    if computerChoiceNumber == 1:
        computerChoiceString = "rock"
    elif computerChoiceNumber == 2:
        computerChoiceString = "paper"
    elif computerChoiceNumber == 3:
        computerChoiceString = "scissors"

    if playerChoiceString == "rock" and computerChoiceString == "scissors" \
    or playerChoiceString == "paper" and computerChoiceString == "rock" \
    or playerChoiceString == "scissors" and computerChoiceString == "paper":
        print(playerName, " chose", playerChoiceString, "  Computer chose", computerChoiceString, " ", playerName, " wins!")
        playerScore += 1
    elif playerChoiceString == "invalid choice":
        print("Please enter a valid letter choice for (R)ock, (P)aper or (S)cissors, or [Q]uit ")
    elif playerQuit is True:
        print("You have quit the game.")
    elif playerChoiceString == computerChoiceString:
        print(playerName, "chose", playerChoiceString, "  Computer chose", computerChoiceString, "  That's a draw!")
    else:
        print(playerName, "chose", playerChoiceString, "  Computer chose", computerChoiceString, "  Computer wins!")
        computerScore += 1

print("Final score: ", playerName, ":", playerScore, "  Computer:", computerScore)
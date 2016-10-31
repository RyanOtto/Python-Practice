#Simulates the powerball.
#From the problem description:
#The first five numbers are drawn from a drum containing 53 balls and the sixth is drawn from a drum containing 42 balls.
#Write a program to generate a set of Powerball numbers by utilizing the choice function in Python's random module.

import random

howManyDrawings = int(input("How many sets of numbers would you like? "))
for drawings in range(0, howManyDrawings):
    randomNum = 0

    firstDrumNum=1
    secondDrumNum=1

    firstDrum = []
    secondDrum=[]

    drumDrawings = []


    for x in range(0, 53):  #Populate first drum's powerball number list
        firstDrum.append(firstDrumNum)
        firstDrumNum += 1
    for x in range(0, 42):  #Populate second drum's powerball number list
        secondDrum.append(secondDrumNum)
        secondDrumNum += 1

    #print(firstDrum)
    #print(secondDrum)

    #Draw the first 5 numbers from first drum
    for x in range(0, 5):
        randomNum=random.choice(firstDrum)
        drumDrawings.append(randomNum)

    #Sixth and final number from second drum
    randomNum=random.choice(secondDrum)
    drumDrawings.append(randomNum)
    drumDrawings[0:5].sort()  #Sort only the first 5 numbers.  The powerball will be output separately.

    print("Your numbers are: ", ", ".join(str(i) for i in drumDrawings[:5]), "Powerball: ", drumDrawings[5])



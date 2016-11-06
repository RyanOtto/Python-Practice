# Prompts user for how many numbers in the Fibonacci sequence they want to see, and prints them
def Fibonaccigenerator():
    fibonnaciInput = int(input("How many fibonacci numbers would you like to generate? "))
    firstFibNum = 0
    secondFibNum = 1
    storedFibNum = 0
    for i in range(fibonnaciInput):
        print(secondFibNum, end=" ")
        storedFibNum = secondFibNum
        secondFibNum += firstFibNum
        firstFibNum = storedFibNum
        
Fibonaccigenerator()
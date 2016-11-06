def Fibonaccigenerator():
    fibonnaciInput = int(input("How many fibonacci numbers would you like to generate? "))
    firstFibNum = 0
    secondFibNum = 1
    storedFibNum = 0
    for i in range(fibonnaciInput):
        storedFibNum = secondFibNum
        secondFibNum += firstFibNum
        firstFibNum = storedFibNum
        

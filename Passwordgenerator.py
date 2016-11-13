# Generate a random password based on user-specified length.  
# The password should include lowercase letters, upercase letters, numbers, and symbols
import random
from random import randint

def Generatepassword(passLength):
    password = ""
    numberList = [int(x) for x in range(0, 9 + 1)]
    lowerLetterList = [chr(x) for x in range(ord('a'), ord('z')+1)]
    upperLetterList = [chr(x) for x in range(ord('A'), ord('Z')+ 1)]
    symbolList = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', 
                  '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', 
                  '|', ':', ':', '"', ',', '<', '.', '>', '?', '/']
    
    for x in range(0, passLength):
        nextEntry = randint(0, 3)
        
        if nextEntry == 0:
            password += str(random.choice(numberList))
        if nextEntry == 1:
            password += random.choice(lowerLetterList)
        if nextEntry == 2:
            password += random.choice(upperLetterList)
        if nextEntry == 3:
            password += random.choice(symbolList)
    
    return password

passLength = int(input("Enter how long you would like your password to be: "))
print ("Password: ", Generatepassword(passLength)) 
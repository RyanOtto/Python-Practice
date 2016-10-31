#Write two functions that convert from celcius to fahrenheit and vice versa.
#Retrieve user input for temperature and which of the two to convert for.

def ctof(cnum):  #Converts from celcius to fahrenheit
    cnum = (cnum * 1.8) + 32
    return cnum;

def ftoc(fnum):  #Converts from fahrenehit to celcius
    fnum = (fnum - 32) / 1.8
    return fnum;

userTemp = float(input("Enter the temperature: "))
userChoice = input("Convert to [F]ahrenheit or [C]elcius? ")

if userChoice == 'c' or  userChoice == 'C':  #If user is converting from fahrenheit to celcius
    print(userTemp, " F=", ftoc(userTemp), "C")

elif userChoice == 'f' or userChoice == 'F':  #If user is converting from celcius to fahrenheit
    print (userTemp, "C =", ctof(userTemp), "F")
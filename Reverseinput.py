# Take user input and reverse it
def Reverse(userString):
    userString = userString[::-1] # Reverses the string received through user input using string slicing
    return userString
        
userString = input("Enter anything you would like reversed: ")
print(Reverse(userString))

#Take a year by the user, and print whether or not that year is a leap year.
def determineleapyear(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 != 0:
            return False

for num in range(0, 2001):
    print(num, "", determineleapyear(num))
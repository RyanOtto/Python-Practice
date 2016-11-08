# Read two text files, and list the duplicate entries.  Also list the number of duplicates for each entry.
# TODO: Put this logic in a method that works with any two files
with open('Resources/happynumbers.txt', 'r') as open_file:
    happyNumbers = open_file.read().split()

with open('Resources/primenumbers.txt', 'r') as open_file:
    primeNumbers = open_file.read().split()

overlapList = []
for i in range(len(primeNumbers)):
    if primeNumbers[i] in happyNumbers:
        overlapList.append(primeNumbers[i])

print("Duplicates: ", ", ".join(str(i) for i in overlapList))
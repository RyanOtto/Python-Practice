# Read two text files, and list the duplicate entries.
# TODO: Change variable names to be more universal
def Checkduplicates(firstFile, secondFile):
    with open(firstFile, 'r') as open_file:
        firstFileContents = open_file.read().split()
    
    with open(secondFile, 'r') as open_file:
        secondFileContents = open_file.read().split()
    
    overlapList = []
    for i in range(len(secondFileContents)):
        if secondFileContents[i] in firstFileContents:
            if not secondFileContents[i] in overlapList:
                overlapList.append(secondFileContents[i])
    return overlapList

print("Duplicates: ", Checkduplicates('Resources/happynumbers.txt', 'Resources/primenumbers.txt'))
print("Duplicates: ", Checkduplicates('Resources/duptextfile1.txt', 'Resources/duptextfile2.txt'))
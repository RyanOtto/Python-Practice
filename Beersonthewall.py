# Print out the lyrics to "beers on the wall"

beersOntheWall=99
for i in range(0,beersOntheWall):
    if beersOntheWall>1: print(str(beersOntheWall) + " bottles of beers on the wall! " + str(beersOntheWall) + " bottles of beer! Take one down, pass it around, " + str(beersOntheWall-1) + (" bottles of beer on the wall! " if beersOntheWall-1 > 1 else " bottle of beer on the wall! "))
    else:
        print(str(beersOntheWall) + " bottle of beer on the wall! " + str(beersOntheWall) + " bottle of beer! Take one down, pass it around, " + str(beersOntheWall) + " bottle of beer on the wall! \nNo more bottles of beer on the wall, no more bottles of beer! Go to the store and buy some more, 99 bottles of beer on the wall!")
    beersOntheWall=beersOntheWall-1
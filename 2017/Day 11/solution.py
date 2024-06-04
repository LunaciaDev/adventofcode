inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split(",")

translationTable = {
    'n': [0, 1],
    'ne': [1, 1],
    'se': [1, 0],
    's': [0, -1],
    'sw': [-1, -1],
    'nw': [-1, 0]
}

# Shifting every other column of a hex grid yield a decent 2D grid that traverse like above

def taskOne(stepList):
    targetVector = [0, 0]

    for step in stepList:
        translated = translationTable[step]
        targetVector[0] += translated[0]
        targetVector[1] += translated[1]

    # Same sign, to get to [x, y] we traverse to the smaller value between x, y
    # Assuming x is smallest, we get to [x, x] taking x steps diagonally,
    # then coming to [x, y] take y - x step horizontally/vertically, totalling y steps which is the bigger one
    if (abs(targetVector[0]) == targetVector[0]) == (abs(targetVector[1]) == targetVector[1]):
        print(max(abs(targetVector[0]), abs(targetVector[1])))
        return
    
    # Different sign, we traverse exclusively on horizontal/vertical axis as diagonal only take you to same sign position
    # Which is a lot longer than travelling on the horizontal/vertical!
    print(abs(targetVector[0]) + abs(targetVector[1]))

def taskTwo(stepList):
    targetVector = [0, 0]
    maxDist = 0

    for step in stepList:
        translated = translationTable[step]
        targetVector[0] += translated[0]
        targetVector[1] += translated[1]

        if (abs(targetVector[0]) == targetVector[0]) == (abs(targetVector[1]) == targetVector[1]):
            maxDist = max(abs(targetVector[0]), abs(targetVector[1]), maxDist)
            continue
        
        maxDist = max(abs(targetVector[0]) + abs(targetVector[1]), maxDist)
    
    print(maxDist)

taskOne(inputStream)
taskTwo(inputStream)

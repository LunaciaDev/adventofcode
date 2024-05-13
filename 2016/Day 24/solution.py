from copy import deepcopy
from itertools import permutations

inputFile = open("input")
inputStream = inputFile.read()
inputStream = inputStream.strip().split("\n")

mainMap = []
startingPositions = [0 for _ in range(8)]

for row in range(len(inputStream)):
    mainMap.append([])

    for cell in range(len(inputStream[row])):
        if inputStream[row][cell] == '#':
            mainMap[row].append(-3)
        elif inputStream[row][cell] == '.':
            mainMap[row].append(-2)
        else: 
            mainMap[row].append(int(inputStream[row][cell]))
            startingPositions[mainMap[row][-1]] = [row, len(mainMap[row]) - 1, 0]

def printMap(map):
    for row in map:
        for cell in row:
            if cell == -3 or cell == -1:
                print('#', end="")
            elif cell == -2:
                print(' ', end="")
            else:
                print(cell, end="")
        print()

def bfs(map, startPos, index):
    localMap = deepcopy(map)
    result = [0 for _ in range(8)]
    foundTarget = 0
    result[index] = -1
    searchQueue = [startPos]

    while foundTarget < 7:
        currentPos = searchQueue.pop(0)
        possibleMoves = [
            [currentPos[0]+1, currentPos[1]],
            [currentPos[0]-1, currentPos[1]],
            [currentPos[0], currentPos[1]+1],
            [currentPos[0], currentPos[1]-1]
        ]

        while len(possibleMoves) > 0:
            currentMove = possibleMoves.pop(0)
            targetCell = localMap[currentMove[0]][currentMove[1]]

            if targetCell == -3 or targetCell == -1:
                continue

            construct = [currentMove[0], currentMove[1], currentPos[-1]+1]
            existInSearch = True

            try:
                searchQueue.index(construct)
            except:
                existInSearch = False

            if targetCell >= 0:
                if targetCell == index:
                    if not existInSearch:
                        searchQueue.append(construct)
                    continue

                if result[targetCell] != 0: 
                    if not existInSearch:
                        searchQueue.append(construct)
                    continue

                result[targetCell] = currentPos[-1] + 1
                foundTarget += 1
            
            if not existInSearch:
                searchQueue.append(construct)
        
        localMap[currentPos[0]][currentPos[1]] = -1
    
    return result

distanceGraph = []
index = 0

for startingPosition in startingPositions:
    distanceGraph.append(bfs(mainMap, startingPosition, index))
    index += 1

def taskOne():
    minLength = 999999999

    for path in permutations(range(1, 8)):
        path = [0] + list(path)
        distance = 0
        for startPointIndex in range(len(path)-1):
            distance += distanceGraph[path[startPointIndex]][path[startPointIndex+1]]
        
        minLength = minLength if minLength < distance else distance

    print(minLength)

def taskTwo():
    minLength = 999999999

    for path in permutations(range(1, 8)):
        path = [0] + list(path) + [0]
        distance = 0
        for startPointIndex in range(len(path)-1):
            distance += distanceGraph[path[startPointIndex]][path[startPointIndex+1]]
        
        minLength = minLength if minLength < distance else distance

    print(minLength)

taskOne()
taskTwo()
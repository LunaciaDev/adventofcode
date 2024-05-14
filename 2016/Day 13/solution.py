from os import system, name
from time import sleep

inputFile = open("input")
inputStream = inputFile.read()

"""
Upping the Ante:

Draw the maze while solving it!
"""

WALL_COLOR = "\033[48;2;65;69;89;1m"
PASSING_COLOR = "\033[48;2;133;193;220m"
CHECKING_COLOR = "\033[48;2;231;130;132m"
FINISH_COLOR = "\033[48;2;166;209;137;1m"
ENDING_SEQUENCE = "\033[0m"

#Sanitizing input
inputStream = int(inputStream)

def getCoordType(x, y):
    number = x*x + 3*x + 2*x*y + y + y*y + inputStream
    oneBitCount = 0
    
    while number > 0:
        oneBitCount += number % 2
        number = int((number - number % 2)/2)
    
    if oneBitCount % 2 == 1:
        return -1

    else: 
        return 0

def drawMazeMap(maze, currentDist):
    if name == 'nt':
        system('cls')
    
    else:
        system('clear')
    
    for row in maze:
        for column in row:
            if column == 0:
                print(' ', end="")
                continue
                
            if column == -1:
                print(WALL_COLOR + ' ' + ENDING_SEQUENCE, end="")
                continue
                
            if column == currentDist:
                print(CHECKING_COLOR + ' ' + ENDING_SEQUENCE, end="")
                continue
            
            if column == -2:
                print(FINISH_COLOR + ' ' + ENDING_SEQUENCE, end="")
            
            print(PASSING_COLOR + ' ' + ENDING_SEQUENCE, end="")
        
        print()

def taskOne(inputStream):
    mazeMap = [
        [getCoordType(0, 0), getCoordType(1, 0)],
        [getCoordType(0, 1), 1]
    ]
    mazeQueue = [[1, 1]]
    currentDist = 1
    locationCount = 1

    while True:
        newQueue = []
        currentDist += 1

        while len(mazeQueue) > 0:
            currentPosition = mazeQueue.pop(0)
            checkPositions = [[currentPosition[0]-1, currentPosition[1]], [currentPosition[0], currentPosition[1]-1], [currentPosition[0]+1, currentPosition[1]], [currentPosition[0], currentPosition[1]+1]]

            while len(checkPositions) > 0:
                checkPosition = checkPositions.pop(0)

                if (checkPosition[0] < 0 or checkPosition[1] < 0): continue

                try:
                    mazeMap[checkPosition[1]][0]
                except:
                    mazeMap.append([])
                
                try:
                    mazeMap[checkPosition[1]][checkPosition[0]]
                except:
                    currentSize = len(mazeMap[checkPosition[1]])
                    for _ in range(checkPosition[0] - currentSize + 1):
                        mazeMap[checkPosition[1]].append(0)

                if (checkPosition[0] == 31 and checkPosition[1] == 39):
                    mazeMap[checkPosition[1]][checkPosition[0]] = -2
                    drawMazeMap(mazeMap, currentDist)
                    print(currentDist - 1)
                    return locationCount

                if (mazeMap[checkPosition[1]][checkPosition[0]] > 0): continue

                mazeMap[checkPosition[1]][checkPosition[0]] = getCoordType(checkPosition[0], checkPosition[1])

                if (mazeMap[checkPosition[1]][checkPosition[0]] == 0):
                    mazeMap[checkPosition[1]][checkPosition[0]] = currentDist
                    if (currentDist-1 <= 50): locationCount += 1
                    newQueue.append(checkPosition)
        
        mazeQueue = newQueue
        drawMazeMap(mazeMap, currentDist)
        sleep(0.3)

print(taskOne(inputStream))

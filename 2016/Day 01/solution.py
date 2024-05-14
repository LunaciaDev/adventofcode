from copy import copy

inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.strip().split(", ")

def taskOne(inputStream):
    coordinate = [0, 0]
    direction = ["+0", "+1", "-0", "-1"]
    currentDirection = 0

    for step in inputStream:
        if step[0] == "L":
            currentDirection -= 1
        else:
            currentDirection += 1
        
        if currentDirection > 3:
            currentDirection = 0
        
        if currentDirection < 0:
            currentDirection = 3
        
        coordinate[int(direction[currentDirection][1])] += int(step[1:]) if direction[currentDirection][0] == "+" else -1 * int(step[1:])

    print(abs(coordinate[0]) + abs(coordinate[1]))

def taskTwo(inputStream):
    currentCoordinate = [300, 300]
    visitedCoordinate = [[False for _ in range(600)] for _ in range(600)]
    visitedCoordinate[100][100] = False
    direction = ["+0", "+1", "-0", "-1"]
    currentDirection = 0

    for step in inputStream:
        if step[0] == "L":
            currentDirection -= 1
        else:
            currentDirection += 1
        
        if currentDirection > 3:
            currentDirection = 0
        
        if currentDirection < 0:
            currentDirection = 3
        
        modifier = 1 if direction[currentDirection][0] == "+" else -1

        for _ in range(int(step[1:])):
            currentCoordinate[int(direction[currentDirection][1])] += modifier

            if visitedCoordinate[currentCoordinate[0]][currentCoordinate[1]]:
                print(abs(currentCoordinate[0]-300) + abs(currentCoordinate[1]-300))
                return
            
            visitedCoordinate[currentCoordinate[0]][currentCoordinate[1]] = True
        
taskOne(inputStream)
taskTwo(inputStream)

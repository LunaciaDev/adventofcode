inputFile = open("input")
inputStream = inputFile.read()

#Helper function to handle Santa movement
def santaMovement(direction, coordinate):
    match direction:
        case "^": coordinate[0] += 1
        case "v": coordinate[0] -= 1
        case ">": coordinate[1] += 1
        case "<": coordinate[1] -= 1
    return coordinate

def taskOne(inputStream):
    houseGrid = [[0 for i in range(200)] for k in range(200)]
    coordinate = [100, 100]
    houseGrid[100][100] = 1
    totalHouseGivenPresent = 1

    for direction in inputStream:
        coordinate = santaMovement(direction, coordinate)
        totalHouseGivenPresent += 1 - houseGrid[coordinate[0]][coordinate[1]]
        houseGrid[coordinate[0]][coordinate[1]] = 1
    
    print(totalHouseGivenPresent)

def taskTwo(inputStream):
    houseGrid = [[0 for i in range(200)] for k in range(200)]
    coordinate = [[100, 100], [100, 100]] #one for Santa, one for Robo-Santa
    houseGrid[100][100] = 1
    totalHouseGivenPresent = 1
    currentTurn = 0 #keep track of whose turn it is currently, 0 for Santa, 1 for Robo-Santa

    for direction in inputStream:
        coordinate[currentTurn] = santaMovement(direction, coordinate[currentTurn])
        totalHouseGivenPresent += 1 - houseGrid[coordinate[currentTurn][0]][coordinate[currentTurn][1]]
        houseGrid[coordinate[currentTurn][0]][coordinate[currentTurn][1]] = 1

        if currentTurn == 0:
            currentTurn = 1
            continue
        currentTurn = 0
    
    print(totalHouseGivenPresent)

taskOne(inputStream)
taskTwo(inputStream)

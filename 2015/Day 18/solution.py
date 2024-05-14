inputFile = open("input")
inputStream = inputFile.read()

LIGHT_GRID_SIZE = 101
STEP = 100

#Sanitizing input
temp = [[0 for _ in range(LIGHT_GRID_SIZE+1)] for _ in range(LIGHT_GRID_SIZE+1)]
inputStream = inputStream.split("\n")

for i in range(1, LIGHT_GRID_SIZE):
    for k in range(1, LIGHT_GRID_SIZE):
        match (inputStream[i-1][k-1]):
            case ".": temp[i][k] = 0
            case "#": temp[i][k] = 1

def lightCheck(inputStream, lightX, lightY):
    total = (-1) * inputStream[lightX][lightY]

    for coordX in range(lightX-1, lightX+2):
        for coordY in range(lightY-1, lightY+2):            
            total += inputStream[coordX][coordY]

    if inputStream[lightX][lightY] == 1:
        if total == 2 or total == 3:
            return 1
        return 0
    
    if total == 3:
        return 1
    return 0


def taskOne(inputStream):
    inputStream = temp

    for step in range(STEP):
        newGrid = [[0 for _ in range(LIGHT_GRID_SIZE+1)] for _ in range(LIGHT_GRID_SIZE+1)]
        for i in range(1, LIGHT_GRID_SIZE):
            for k in range(1, LIGHT_GRID_SIZE):
                newGrid[i][k] = lightCheck(inputStream, i, k)
        
        inputStream = newGrid
    
    print(sum([sum(i) for i in inputStream]))

def taskTwo(inputStream):
    inputStream = temp
    inputStream[100][1] = 1

    for step in range(STEP):
        newGrid = [[0 for _ in range(LIGHT_GRID_SIZE+1)] for _ in range(LIGHT_GRID_SIZE+1)]
        for i in range(1, LIGHT_GRID_SIZE):
            for k in range(1, LIGHT_GRID_SIZE):
                if (i == 1 or i == 100) and (k == 1 or k == 100): 
                    newGrid[i][k] = 1
                    continue

                newGrid[i][k] = lightCheck(inputStream, i, k)
        
        inputStream = newGrid
    
    print(sum([sum(i) for i in inputStream]))

taskOne(inputStream)
taskTwo(inputStream)

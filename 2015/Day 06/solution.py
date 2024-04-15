inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")

for index in range(len(inputStream)):
    inputStream[index] = inputStream[index].split(" ")
    if len(inputStream[index]) == 5: 
        inputStream[index] = inputStream[index][1:6]
    inputStream[index] = [inputStream[index][0], inputStream[index][1].split(","), inputStream[index][3].split(",")]

def taskOne(inputStream):
    def inversion(num):
        return 1 - num

    def toggleOn(num):
        return 1

    def toggleOff(num):
        return 0

    lightGrid = [[0 for i in range(1000)] for i in range(1000)]
    for instruction in inputStream:
        action = 0

        match instruction[0]:
            case "on": action = toggleOn
            case "off": action = toggleOff
            case "toggle": action = inversion
        
        for coordX in range(int(instruction[1][0]), int(instruction[2][0])+1):
            for coordY in range(int(instruction[1][1]), int(instruction[2][1])+1):
                lightGrid[coordX][coordY] = action(lightGrid[coordX][coordY])

    print(sum([sum(item) for item in lightGrid]))

def taskTwo(inputStream):
    lightGrid = [[0 for i in range(1000)] for i in range(1000)]
    for instruction in inputStream:

        match instruction[0]:
            case "on": action = 1
            case "off": action = -1
            case "toggle": action = 2
        
        for coordX in range(int(instruction[1][0]), int(instruction[2][0])+1):
            for coordY in range(int(instruction[1][1]), int(instruction[2][1])+1):
                lightGrid[coordX][coordY] += action
                if lightGrid[coordX][coordY] < 0: lightGrid[coordX][coordY] = 0

    print(sum([sum(item) for item in lightGrid]))


taskOne(inputStream)
taskTwo(inputStream)

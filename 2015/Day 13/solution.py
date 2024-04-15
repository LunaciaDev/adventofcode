import copy

inputFile = open("input")
inputStream = inputFile.read()
inputStream = inputStream.split("\n")

def taskOne(inputStream):
    guest = {
        "Alice": 0,
        "Bob": 1,
        "Carol": 2,
        "David": 3,
        "Eric": 4,
        "Frank": 5,
        "George": 6,
        "Mallory": 7
    }

    happinessMatrix = [[0 for _ in range(8)] for _ in range(8)]

    for line in inputStream:
        line = line.strip(".").split()
        happinessMatrix[guest[line[0]]][guest[line[-1]]] = int(line[3]) * (1 if line[2] == "gain" else -1)

    def happinessCalc(seatingList):
        happiness = happinessMatrix[seatingList[0]][seatingList[-1]] + happinessMatrix[seatingList[0]][seatingList[1]]
        happiness += happinessMatrix[seatingList[-1]][seatingList[-2]] + happinessMatrix[seatingList[-1]][seatingList[0]]

        for index in range(1, len(seatingList)-1):
            happiness += happinessMatrix[seatingList[index]][seatingList[index-1]] + happinessMatrix[seatingList[index]][seatingList[index+1]]

        return happiness

    def recursiveSolver(unseatedList, seatingList):
        maxHappiness = -16000
        if len(unseatedList) == 0:
            return happinessCalc(seatingList)

        for person in unseatedList:
            nextSeatingList = copy.copy(seatingList)
            nextUnseatedList = copy.copy(unseatedList)
            nextUnseatedList.remove(person)
            nextSeatingList.append(person)
            tempHappiness = recursiveSolver(nextUnseatedList, nextSeatingList)

            if tempHappiness > maxHappiness:
                maxHappiness = tempHappiness

        return maxHappiness
    
    print(recursiveSolver([1, 2, 3, 4, 5, 6, 7], [0])) #709

def taskTwo(inputStream):
    guest = {
        "Me": 0,
        "Alice": 1,
        "Bob": 2,
        "Carol": 3,
        "David": 4,
        "Eric": 5,
        "Frank": 6,
        "George": 7,
        "Mallory": 8
    }

    happinessMatrix = [[0 for _ in range(9)] for _ in range(9)]

    for line in inputStream:
        line = line.strip(".").split()
        happinessMatrix[guest[line[0]]][guest[line[-1]]] = int(line[3]) * (1 if line[2] == "gain" else -1)

    def happinessCalc(seatingList):
        happiness = happinessMatrix[seatingList[0]][seatingList[-1]] + happinessMatrix[seatingList[0]][seatingList[1]]
        happiness += happinessMatrix[seatingList[-1]][seatingList[-2]] + happinessMatrix[seatingList[-1]][seatingList[0]]

        for index in range(1, len(seatingList)-1):
            happiness += happinessMatrix[seatingList[index]][seatingList[index-1]] + happinessMatrix[seatingList[index]][seatingList[index+1]]

        return happiness

    def recursiveSolver(unseatedList, seatingList):
        maxHappiness = -16000
        if len(unseatedList) == 0:
            return happinessCalc(seatingList)

        for person in unseatedList:
            nextSeatingList = copy.copy(seatingList)
            nextUnseatedList = copy.copy(unseatedList)
            nextUnseatedList.remove(person)
            nextSeatingList.append(person)
            tempHappiness = recursiveSolver(nextUnseatedList, nextSeatingList)

            if tempHappiness > maxHappiness:
                maxHappiness = tempHappiness

        return maxHappiness
    
    print(recursiveSolver([1, 2, 3, 4, 5, 6, 7, 8], [0])) #668


taskOne(inputStream)
taskTwo(inputStream)

from copy import deepcopy

inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split("\n")

for index in range(len(inputStream)):
    inputStream[index] = int(inputStream[index])

def taskOne(inputStream):
    instructionSet = deepcopy(inputStream)
    programCounter = 0
    maxPC = len(inputStream)
    stepCount = 0

    while programCounter > -1 and programCounter < maxPC:
        instructionSet[programCounter] += 1
        programCounter += instructionSet[programCounter] - 1
        stepCount += 1

    print(stepCount)

def taskTwo(inputStream):
    instructionSet = deepcopy(inputStream)
    programCounter = 0
    maxPC = len(inputStream)
    stepCount = 0

    while programCounter > -1 and programCounter < maxPC:
        oldPC = programCounter
        programCounter += instructionSet[programCounter]
        instructionSet[oldPC] += 1 if instructionSet[oldPC] < 3 else -1
        stepCount += 1

    print(stepCount)

taskOne(inputStream)
taskTwo(inputStream)
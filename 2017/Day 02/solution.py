from itertools import combinations
from math import floor, ceil

inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split("\n")

for lineIndex in range(len(inputStream)):
    inputStream[lineIndex] = inputStream[lineIndex].split("\t")
    for itemIndex in range(len(inputStream[lineIndex])):
        inputStream[lineIndex][itemIndex] = int(inputStream[lineIndex][itemIndex])

def taskOne(inputStream):
    checkSum = 0

    for row in inputStream:
        minVal = min(row)
        maxVal = max(row)
        checkSum += maxVal - minVal
    
    print(checkSum)

def taskTwo(inputStream):
    sumVal = 0

    for row in inputStream:
        for pair in combinations(row, 2):
            maxVal = max(pair)
            minVal = min(pair)
            divResult = maxVal / minVal

            if floor(divResult) == ceil(divResult):
                sumVal += floor(divResult)
                break

    print(sumVal)

taskOne(inputStream)
taskTwo(inputStream)

from math import floor

inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split("\n")
for index in range(len(inputStream)):
    inputStream[index] = inputStream[index].split(": ")
    inputStream[index][0] = int(inputStream[index][0])
    inputStream[index][1] = int(inputStream[index][1])

rangeList = [0 for _ in range(inputStream[-1][0] + 1)]

for layer in inputStream:
    rangeList[layer[0]] = layer[1]

def taskOne(rangeList):
    scannerList = [0 for _ in range(len(rangeList))]
    direction = [1 for _ in range(len(rangeList))]
    severity = 0
    
    for position in range(len(scannerList)):
        if scannerList[position] == 0:
            severity += rangeList[position] * position
        
        for scannerIndex in range(len(scannerList)):
            if rangeList[scannerIndex] == 0: continue

            scannerList[scannerIndex] = scannerList[scannerIndex] + direction[scannerIndex]
            if scannerList[scannerIndex] + 1 == rangeList[scannerIndex] or scannerList[scannerIndex] == 0:
                direction[scannerIndex] *= -1
    
    print(severity)

# When we shift forward k picosecond with n possible positions from position 0
# First we take k % (2n - 2), this return the smallest amount of step not becoming a cycle, call it c
# floor(c / (n-1)), if it's 0, we move to position c, if it's 1, we move to position n - (c - n + 1) - 1
# Remember to flip the direction accordingly!

def taskTwo(rangeList):
    futurePositionList = [0 for _ in range(len(rangeList))]
    direction = [1 for _ in range(len(rangeList))]
    
    for index in range(len(futurePositionList)):
        if rangeList[index] == 0: 
            futurePositionList[index] = 1
            continue

        minNonCycleSteps = index % (2 * rangeList[index] - 2)

        if floor(minNonCycleSteps / (rangeList[index] - 1)) == 0:
            futurePositionList[index] = minNonCycleSteps
            continue

        futurePositionList[index] = rangeList[index] - (minNonCycleSteps - rangeList[index] + 1) - 1
        if futurePositionList[index] != 0:
            direction[index] *= -1

    timeWaited = 0

    while True:
        if min(futurePositionList) != 0:
            break

        timeWaited += 1

        for scannerIndex in range(len(futurePositionList)):
            if rangeList[scannerIndex] == 0: continue

            futurePositionList[scannerIndex] = futurePositionList[scannerIndex] + direction[scannerIndex]
            if futurePositionList[scannerIndex] + 1 == rangeList[scannerIndex] or futurePositionList[scannerIndex] == 0:
                direction[scannerIndex] *= -1
    
    print(timeWaited)


taskOne(rangeList)
taskTwo(rangeList)
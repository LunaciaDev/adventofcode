from math import lcm

inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split("\n")

discInformation = []

for disc in inputStream:
    disc = disc.split(" ")
    discInformation.append([int(disc[3]), int(disc[-1][:-1])])

def taskOne(inputStream):
    minimumTime = 0
    revVal = 1
    discOffset = 1

    for disc in discInformation:
        currentDiscPosition = (disc[1] + minimumTime) % disc[0]
        targetPosition = disc[0] - discOffset
        if targetPosition < 0: targetPosition += disc[0]

        while currentDiscPosition != targetPosition:
            minimumTime += revVal
            currentDiscPosition += revVal
            currentDiscPosition %= disc[0]
        
        revVal = lcm(revVal, disc[0])
        discOffset += 1
    
    return minimumTime

def taskTwo(inputStream):
    discInformation.append([11, 0])
    
    minimumTime = 0
    revVal = 1
    discOffset = 1

    for disc in discInformation:
        currentDiscPosition = (disc[1] + minimumTime) % disc[0]
        targetPosition = disc[0] - discOffset
        if targetPosition < 0: targetPosition += disc[0]

        while currentDiscPosition != targetPosition:
            minimumTime += revVal
            currentDiscPosition += revVal
            currentDiscPosition %= disc[0]
        
        revVal = lcm(revVal, disc[0])
        discOffset += 1
    
    return minimumTime

print(taskOne(inputStream))
print(taskTwo(inputStream))
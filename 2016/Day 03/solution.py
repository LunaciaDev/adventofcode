import math as m

inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.strip().split("\n")
for index in range(len(inputStream)):
    inputStream[index] = inputStream[index].strip().split(" ")
    for sideIndex in range(len(inputStream[index])):
        inputStream[index][sideIndex] = int(inputStream[index][sideIndex])

def checkTriangle(firstSide, secondSide, thirdSide):
    return firstSide + secondSide > thirdSide and firstSide + thirdSide > secondSide and secondSide + thirdSide > firstSide


def taskOne(inputStream):
    triangleCount = 0

    for triangle in inputStream:

        if not checkTriangle(triangle[0], triangle[1], triangle[2]): continue

        triangleCount += 1

    print(triangleCount)

def taskTwo(inputStream):
    triangles = []
    triangleCount = 0
    lineCount = 0

    for _ in range(3):
        triangles.append([])

    for triplet in inputStream:
        index = 0

        for side in triplet:
            triangles[index].append(side)
            index += 1

        lineCount += 1    
        
        if lineCount != 3: continue

        lineCount = 0

        for index in range(len(triangles)):
            foundTriangle = triangles[index]

            if checkTriangle(foundTriangle[0], foundTriangle[1], foundTriangle[2]): triangleCount += 1

            triangles[index] = []
    
    print(triangleCount)

taskOne(inputStream)
taskTwo(inputStream)
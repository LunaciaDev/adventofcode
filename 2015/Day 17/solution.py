import copy
from itertools import combinations

inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")
for index in range(len(inputStream)):
    inputStream[index] = int(inputStream[index])
inputStream.sort(reverse=True)

'''
Because taking 3 biggest container (47, 46, 44) still doesn't exceed the required
capacity (150), we start searching from depth = 4.
'''

def taskOne(inputStream):
    combinationCount = 0

    for size in range(4, len(inputStream)):
        for containerSet in combinations(inputStream, size):
            if sum(containerSet) == 150:
                combinationCount += 1

    print(combinationCount)

def taskTwo(inputStream):
    combinationCount = 0
    flag = False

    for size in range(4, len(inputStream)):
        if flag: break

        for containerSet in combinations(inputStream, size):
            if sum(containerSet) == 150:
                flag = True
                combinationCount += 1

    print(combinationCount)

taskOne(inputStream)
taskTwo(inputStream)
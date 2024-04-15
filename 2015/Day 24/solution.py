from copy import copy
from itertools import combinations

inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.strip().split("\n")
for index in range(len(inputStream)):
    inputStream[index] = int(inputStream[index])

inputStream.sort(reverse=True)

def taskOne(inputStream):
    flag = False
    minQE = 1000000000000
    BALANCE_WEIGHT = sum(inputStream) // 3
    
    #Need at least 6 for weight > balance_weight
    for i in range(6, len(inputStream)):
        if flag: break
        for packageSet in combinations(inputStream, i):
            if sum(packageSet) == BALANCE_WEIGHT:
                flag = True
                tempQE = 1

                for package in packageSet:
                    tempQE = tempQE * package
                
                if tempQE < minQE:
                    minQE = tempQE
    
    print(minQE)

def taskTwo(inputStream):
    flag = False
    minQE = 1000000000000
    BALANCE_WEIGHT = sum(inputStream) // 4
    
    #Need at least 4 for weight > balance_weight
    for i in range(4, len(inputStream)):
        if flag: break
        for packageSet in combinations(inputStream, i):
            if sum(packageSet) == BALANCE_WEIGHT:
                flag = True
                tempQE = 1

                for package in packageSet:
                    tempQE = tempQE * package
                
                if tempQE < minQE:
                    minQE = tempQE
    
    print(minQE)

taskOne(inputStream)
taskTwo(inputStream)

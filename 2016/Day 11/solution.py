from itertools import combinations
from copy import deepcopy

#TODO: Clear up this mess.

"""
BFS with pruning.

We prune based on the "hash" of the states, generated from the object count of each floor, plus which floor the elevator is at.
Also the solver try to solve with the condition that we shall ONLY bring one object back from the higher floors.
"""

FLOOR_COUNT = 4

def verifyPosition(state, floorsToCheck):
    for floor in floorsToCheck:
        floor = state[floor]

        generator = floor["generator"]
        microchip = floor["microchip"]
        existGenerator = sum(generator) > 0

        for i in range(len(generator)):
            if microchip[i] == 1 and generator[i] == 0:
                if existGenerator: return False
    
    return True

def generateHash(state):
    hashList = []

    for i in range(FLOOR_COUNT):
        # It does not matter what type of object the current floor has, only the count should matter.
        hashList.append(str(sum(state[i]["generator"])))
        hashList.append(str(sum(state[i]["microchip"])))
    
    # has to add the information of where this hash happened since the same state could happen on different part of the solution
    hashList.append(str(state["currentPosition"]))
    return "".join(hashList)

def exploreFloors(startingState, objectCount):
    visitedStateHash = [generateHash(startingState)]
    stateQueue = [startingState]
    
    while True:
        currentState = stateQueue.pop(0)

        currentFloor = currentState[currentState["currentPosition"]]
        currentFloorNum = currentState["currentPosition"]
        generatorIndexList = []
        microchipIndexList = []
        targetFloors = [currentFloorNum-1, currentFloorNum+1]

        for i in range(len(currentFloor["generator"])):
            if currentFloor["generator"][i] == 1: generatorIndexList.append(i)
        
        for i in range(len(currentFloor["microchip"])):
            if currentFloor["microchip"][i] == 1: microchipIndexList.append(i)

        combinationGenerator = list(range(len(generatorIndexList) + len(microchipIndexList)))
        generatorLimit = len(generatorIndexList)

        while len(targetFloors) > 0:
            targetFloor = targetFloors.pop(0)
            if targetFloor > FLOOR_COUNT-1 or targetFloor < 0: continue

            if targetFloor < currentFloorNum:
                # Do not bother bringing item to disabled floor.
                if currentState["disabledFloor"][targetFloor]: continue

                # Bring only one item down.
                for generator in generatorIndexList:
                    newState = deepcopy(currentState)
                    newState[currentFloorNum]["generator"][generator] = 0
                    newState[targetFloor]["generator"][generator] = 1
                    newState["stepTaken"] = currentState["stepTaken"] + 1
                    newState["currentPosition"] = targetFloor

                    newStateHash = generateHash(newState)
                    hasVisited = True

                    try:
                        visitedStateHash.index(newStateHash)
                    except:
                        hasVisited = False
                    
                    if hasVisited: continue

                    if not verifyPosition(newState, [currentFloorNum, targetFloor]): continue

                    stateQueue.append(newState)
                    visitedStateHash.append(newStateHash)
                
                for microchip in microchipIndexList:
                    newState = deepcopy(currentState)
                    newState[currentFloorNum]["microchip"][microchip] = 0
                    newState[targetFloor]["microchip"][microchip] = 1
                    newState["stepTaken"] = currentState["stepTaken"] + 1
                    newState["currentPosition"] = targetFloor

                    newStateHash = generateHash(newState)
                    hasVisited = True

                    try:
                        visitedStateHash.index(newStateHash)
                    except:
                        hasVisited = False
                    
                    if hasVisited: continue

                    if not verifyPosition(newState, [currentFloorNum, targetFloor]): continue

                    stateQueue.append(newState)
                    visitedStateHash.append(newStateHash)

            else:
                for generator in generatorIndexList:
                    newState = deepcopy(currentState)
                    newState[currentFloorNum]["generator"][generator] = 0
                    newState[targetFloor]["generator"][generator] = 1
                    newState["stepTaken"] = currentState["stepTaken"] + 1
                    newState["currentPosition"] = targetFloor

                    newStateHash = generateHash(newState)
                    hasVisited = True

                    try:
                        visitedStateHash.index(newStateHash)
                    except:
                        hasVisited = False
                    
                    if hasVisited: continue

                    if not verifyPosition(newState, [currentFloorNum, targetFloor]): continue

                    stateQueue.append(newState)
                    visitedStateHash.append(newStateHash)
                
                for microchip in microchipIndexList:
                    newState = deepcopy(currentState)
                    newState[currentFloorNum]["microchip"][microchip] = 0
                    newState[targetFloor]["microchip"][microchip] = 1
                    newState["stepTaken"] = currentState["stepTaken"] + 1
                    newState["currentPosition"] = targetFloor

                    newStateHash = generateHash(newState)
                    hasVisited = True

                    try:
                        visitedStateHash.index(newStateHash)
                    except:
                        hasVisited = False
                    
                    if hasVisited: continue

                    if not verifyPosition(newState, [currentFloorNum, targetFloor]): continue

                    stateQueue.append(newState)
                    visitedStateHash.append(newStateHash)

                for selection in combinations(combinationGenerator, 2):
                    newState = deepcopy(currentState)
                    newState["stepTaken"] = currentState["stepTaken"] + 1
                    newState["currentPosition"] = targetFloor

                    for selectedThing in selection:
                        if selectedThing >= generatorLimit:
                            selectedThing -= generatorLimit
                            newState[currentFloorNum]["microchip"][microchipIndexList[selectedThing]] = 0
                            newState[targetFloor]["microchip"][microchipIndexList[selectedThing]] = 1

                        else:
                            newState[currentFloorNum]["generator"][generatorIndexList[selectedThing]] = 0
                            newState[targetFloor]["generator"][generatorIndexList[selectedThing]] = 1
                        
                    if sum(newState[targetFloor]["generator"]) + sum(newState[targetFloor]["microchip"]) == objectCount and targetFloor == FLOOR_COUNT-1:
                        return newState["stepTaken"]

                    newStateHash = generateHash(newState)
                    hasVisited = True

                    try:
                        visitedStateHash.index(newStateHash)
                    except:
                        hasVisited = False
                    
                    if hasVisited: continue

                    if not verifyPosition(newState, [currentFloorNum, targetFloor]): continue

                    if sum(newState[currentFloorNum]["microchip"]) + sum(newState[currentFloorNum]["generator"]) == 0:
                        if currentFloorNum == 0:
                            # Disable when it's the first floor
                            newState["disabledFloor"][currentFloorNum] = True
                        elif newState["disabledFloor"][currentFloorNum - 1]:
                            # Disable if the previous floor is also disabled
                            newState["disabledFloor"][currentFloorNum] = True

                    stateQueue.append(newState)
                    visitedStateHash.append(newStateHash)


def taskOne():
    objectCount = 10

    startingState = {
        0: {
            "generator": [1, 1, 0, 0, 0],
            "microchip": [1, 1, 0, 0, 0]
        },
        1: {
            "generator": [0, 0, 1, 1, 1],
            "microchip": [0, 0, 0, 1, 1]
        },
        2: {
            "generator": [0, 0, 0, 0, 0],
            "microchip": [0, 0, 1, 0, 0]
        },
        3: {
            "generator": [0, 0, 0, 0, 0],
            "microchip": [0, 0, 0, 0, 0]
        },
        "stepTaken": 0,
        "currentPosition": 0,
        "disabledFloor": [False, False, False, False]
    }

    print(exploreFloors(startingState, objectCount))

def taskTwo():
    objectCount = 14

    startingState = {
        0: {
            "generator": [1, 1, 0, 0, 0, 1, 1],
            "microchip": [1, 1, 0, 0, 0, 1, 1]
        },
        1: {
            "generator": [0, 0, 1, 1, 1, 0, 0],
            "microchip": [0, 0, 0, 1, 1, 0, 0]
        },
        2: {
            "generator": [0, 0, 0, 0, 0, 0, 0],
            "microchip": [0, 0, 1, 0, 0, 0, 0]
        },
        3: {
            "generator": [0, 0, 0, 0, 0, 0, 0],
            "microchip": [0, 0, 0, 0, 0, 0, 0],
        },
        "stepTaken": 0,
        "currentPosition": 0,
        "disabledFloor": [False, False, False, False]
    }

    print(exploreFloors(startingState, objectCount))

taskOne()
taskTwo()
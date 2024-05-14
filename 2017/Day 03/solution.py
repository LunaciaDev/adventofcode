from math import pow, floor

inputFile = open("input")
inputStream = int(inputFile.read())

"""
The bottom right corner value is the sequence of oddNum^2 which is also the maximum value in a ring.
559^2 = 312481 > 312051 > 558^2 = 311364

From this value, we can get the value of all 4 corner by subtracting with the root of the bottom-right corner, minus 1.
"""

def taskOne(inputStream):
    if inputStream == 1: return 0
    # Find the ring where the number belong
    ringNum = 3

    while True:
        if pow(ringNum, 2) > inputStream and pow(ringNum-2, 2) < inputStream: break
        ringNum += 2

    maxValRing = pow(ringNum, 2)

    # Find the side where the number is at
    offsets = [(1, 0), (2, 1), (3, 2)]
    selectedOffset = None

    for offset in offsets:
        if maxValRing - (ringNum-1)*offset[0] < inputStream and maxValRing - (ringNum-1)*offset[1] > inputStream:
            selectedOffset = offset
            break
    else:
        selectedOffset = (0, 3)

    # Calculate the distance from the number to the middle value of the side
    midVal = int((maxValRing - (ringNum-1)*selectedOffset[1]) - floor(ringNum / 2))
    distToMiddle = max(midVal, inputStream) - min(midVal, inputStream)
    distToCenter = distToMiddle + int(floor(ringNum / 2))

    print(distToCenter)

def taskTwo(inputStream):
    memory = [[0 for _ in range(19)] for _ in range(19)]
    memory[9][9] = 1
    ptr = (9, 10)
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    counter = 0
    group = 0
    ring = 3

    while True:
        adjacency = [
            memory[ptr[0]+1][ptr[1]],
            memory[ptr[0]+1][ptr[1]+1],
            memory[ptr[0]+1][ptr[1]-1],
            memory[ptr[0]-1][ptr[1]],
            memory[ptr[0]-1][ptr[1]+1],
            memory[ptr[0]-1][ptr[1]-1],
            memory[ptr[0]][ptr[1]+1],
            memory[ptr[0]][ptr[1]-1],
        ]

        memory[ptr[0]][ptr[1]] = sum(adjacency)
        if memory[ptr[0]][ptr[1]] > inputStream:
            print(memory[ptr[0]][ptr[1]])
            return

        if counter == ring-2:
            if group != 3:
                group += 1
                counter = 0
                ptr = (ptr[0] + direction[group][0], ptr[1] + direction[group][1])
                continue
            
            counter = 0
            ptr = (ptr[0] + direction[group][0], ptr[1] + direction[group][1])
            group = 0
            ring += 2
            continue
        
        counter += 1
        ptr = (ptr[0] + direction[group][0], ptr[1] + direction[group][1])

taskOne(inputStream)
taskTwo(inputStream)
from copy import copy

inputFile = open("input")
inputStream = inputFile.read().strip().split(",")

for index in range(len(inputStream)):
    match(inputStream[index][0]):
        case 's':
            inputStream[index] = [inputStream[index][0], 16 - int(inputStream[index][1:])]

        case 'x':
            temp = inputStream[index][1:].split("/")
            inputStream[index] = [inputStream[index][0], [int(temp[0]), int(temp[1])]]

        case 'p':
            temp = inputStream[index][1:].split("/")
            inputStream[index] = [inputStream[index][0], [temp[0], temp[1]]]

def taskOne(inputStream):
    positions = [chr(i) for i in range(97, 97 + 16)]

    for moves in inputStream:
        match (moves[0]):
            case 's':
                positions = positions[moves[1]:] + positions[:moves[1]]
            
            case 'x':
                positions[moves[1][0]], positions[moves[1][1]] = positions[moves[1][1]], positions[moves[1][0]]

            case 'p':
                swapIndex = -1

                for index in range(len(positions)):
                    try:
                        moves[1].index(positions[index])
                    except:
                        continue

                    if swapIndex < 0:
                        swapIndex = index
                        continue

                    positions[swapIndex], positions[index] = positions[index], positions[swapIndex]
                    break

    print("".join(positions))

def findCycles(inputStream):
    """
    I do not deny the fact that I almost wrote a brute-force approach to this.
    """
    positions = [chr(i) for i in range(97, 97 + 16)]
    cache = {}

    for step in range(1000000000):
        temp = "".join(positions)
        res = cache.get(temp, None)

        if (res is not None):
            print(f"Cache hit at step {step}, key {temp}")
            if (step > 70): return
            positions = copy(res)
            continue

        for moves in inputStream:
            match (moves[0]):
                case 's':
                    positions = positions[moves[1]:] + positions[:moves[1]]
                
                case 'x':
                    positions[moves[1][0]], positions[moves[1][1]] = positions[moves[1][1]], positions[moves[1][0]]

                case 'p':
                    swapIndex = -1

                    for index in range(len(positions)):
                        try:
                            moves[1].index(positions[index])
                        except:
                            continue

                        if swapIndex < 0:
                            swapIndex = index
                            continue

                        positions[swapIndex], positions[index] = positions[index], positions[swapIndex]
                        break
        
        cache[temp] = copy(positions)

def taskTwo(inputStream):
    positions = [chr(i) for i in range(97, 97 + 16)]

    for _ in range(1000000000 % 30):
        for moves in inputStream:
            match (moves[0]):
                case 's':
                    positions = positions[moves[1]:] + positions[:moves[1]]
                
                case 'x':
                    positions[moves[1][0]], positions[moves[1][1]] = positions[moves[1][1]], positions[moves[1][0]]

                case 'p':
                    swapIndex = -1

                    for index in range(len(positions)):
                        try:
                            moves[1].index(positions[index])
                        except:
                            continue

                        if swapIndex < 0:
                            swapIndex = index
                            continue

                        positions[swapIndex], positions[index] = positions[index], positions[swapIndex]
                        break

    print("".join(positions))

taskOne(inputStream)
taskTwo(inputStream)
inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.strip().split("\n")

def taskOne(inputStream):
    numpad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    password = ""
    pointer = [1, 1]

    for instructionSet in inputStream:
        for instruction in instructionSet:
            match instruction:
                case "U":
                    if pointer[0] == 0: continue
                    pointer[0] -= 1
                
                case "D":
                    if pointer[0] == 2: continue
                    pointer[0] += 1

                case "L":
                    if pointer[1] == 0: continue
                    pointer[1] -= 1
                
                case "R":
                    if pointer[1] == 2: continue
                    pointer[1] += 1
                
        password = password + str(numpad[pointer[0]][pointer[1]])
    
    print(password) #78985

def taskTwo(inputStream):
    numpad = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 2, 3, 4, 0, 0],
        [0, 5, 6, 7, 8, 9, 0],
        [0, 0, "A", "B", "C", 0, 0],
        [0, 0, 0, "D", 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    password = ""
    pointer = [2, 1]

    for instructionSet in inputStream:
        for instruction in instructionSet:
            match instruction:
                case "U":
                    if numpad[pointer[0] - 1][pointer[1]] == 0: continue
                    pointer[0] -= 1
                
                case "D":
                    if numpad[pointer[0] + 1][pointer[1]] == 0: continue
                    pointer[0] += 1

                case "L":
                    if numpad[pointer[0]][pointer[1] - 1] == 0: continue
                    pointer[1] -= 1
                
                case "R":
                    if numpad[pointer[0]][pointer[1] + 1] == 0: continue
                    pointer[1] += 1
                
        password = password + str(numpad[pointer[0]][pointer[1]])
    
    print(password) #57DD8

taskOne(inputStream)
taskTwo(inputStream)

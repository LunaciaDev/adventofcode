inputFile = open("input")
inputStream = inputFile.read()

instructionSet = {
    "hlf": 0, #Half x
    "tpl": 1, #Triple x
    "inc": 2, #Increment x
    "jmp": 3, #Jump offset
    "jie": 4, #Jump if even
    "jio": 5, #Junp if one
}

registerName = {
    "a": 0,
    "b": 1
}

#Sanitizing input
inputStream = inputStream.strip().split("\n")

for index in range(len(inputStream)):
    inputStream[index] = inputStream[index].split(" ")
    inputStream[index][0] = instructionSet[inputStream[index][0]]
    if inputStream[index][0] != 3:
        inputStream[index][1] = registerName[inputStream[index][1]]

def executeInstruction(pointer, register):
    instruction = inputStream[pointer]

    match (instruction[0]):
        case 0: 
            register[instruction[1]] = register[instruction[1]] // 2
            return pointer + 1

        case 1:
            register[instruction[1]] = register[instruction[1]] * 3
            return pointer + 1

        case 2:
            register[instruction[1]] = register[instruction[1]] + 1
            return pointer + 1

        case 3:
            modifier = -1 if instruction[1][0] == "-" else 1
            return pointer + modifier * int(instruction[1][1:])

        case 4:
            if register[instruction[1]] % 2 != 0: 
                return pointer + 1

            modifier = -1 if instruction[2][0] == "-" else 1
            return pointer + modifier * int(instruction[2][1:])

        case 5:
            if register[instruction[1]] != 1: 
                return pointer + 1

            modifier = -1 if instruction[2][0] == "-" else 1
            return pointer + modifier * int(instruction[2][1:])

def taskOne(inputStream):
    pointer = 0
    register = [0, 0]

    while pointer < len(inputStream) and pointer >= 0: 
        pointer = executeInstruction(pointer, register)
    
    print(register[1])
    

def taskTwo(inputStream):
    pointer = 0
    register = [1, 0]

    while pointer < len(inputStream) and pointer >= 0: 
        pointer = executeInstruction(pointer, register)
    
    print(register[1])


taskOne(inputStream)
taskTwo(inputStream)

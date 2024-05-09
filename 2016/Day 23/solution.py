from copy import deepcopy

inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split("\n")

for inputStreamIndex in range(len(inputStream)):
    inputStream[inputStreamIndex] = inputStream[inputStreamIndex].split(" ")

inputStreamBackup = deepcopy(inputStream)

def executeProgram(registers):
    instructionCount = len(inputStream)
    programCounter = 0

    while programCounter < instructionCount:
        instruction = inputStream[programCounter]

        try:
            match instruction[0][0]:
                case 'c': # copy function
                    value = None

                    try:
                        value = int(instruction[1])
                    except:
                        value = registers[instruction[1]]

                    registers[instruction[2]] = value
                    
                case 'i': # increment instruction
                    registers[instruction[1]] += 1
                
                case 'd': # decrement instruction
                    registers[instruction[1]] -= 1
                
                case 'j': # jump on not zero instruction
                    jumpAmount = None
                    condition = None

                    try:
                        jumpAmount = int(instruction[2])
                    except:
                        jumpAmount = registers[instruction[2]]

                    try:
                        condition = int(instruction[1])
                    except:
                        condition = registers[instruction[1]]

                    if condition != 0:
                        programCounter += jumpAmount
                        continue
                
                case 't': # toggle instruction
                    shiftAmount = registers[instruction[1]]
                    
                    if (programCounter + shiftAmount > instructionCount): 
                        programCounter += 1
                        continue

                    targetInstruction = inputStream[programCounter + shiftAmount]

                    if len(targetInstruction) == 2:
                        if targetInstruction[0][0] == 'i':
                            inputStream[programCounter + shiftAmount][0] = 'd'
                        else: inputStream[programCounter + shiftAmount][0] = 'i'
                    else:
                        if targetInstruction[0][0] == 'j':
                            inputStream[programCounter + shiftAmount][0] = 'c'
                        else: inputStream[programCounter + shiftAmount][0] = 'j'
                    

        except:
            programCounter += 1
            continue
        
        programCounter += 1

    return registers

def taskOne(inputStream):
    registers = {
        'a': 7,
        'b': 0,
        'c': 0,
        'd': 0
    }

    registers = executeProgram(registers)

    print(registers['a'])

def taskTwo(inputStream):
    registers = {
        'a': 12,
        'b': 0,
        'c': 0,
        'd': 0
    }

    registers = executeProgram(registers)

    print(registers['a'])

taskOne(inputStream)
inputStream = inputStreamBackup
taskTwo(inputStream)

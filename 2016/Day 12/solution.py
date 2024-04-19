inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.strip().split("\n")

for inputStreamIndex in range(len(inputStream)):
    inputStream[inputStreamIndex] = inputStream[inputStreamIndex].split(" ")

def executeProgram(registers):
    instructionCount = len(inputStream)
    programCounter = 0

    while programCounter < instructionCount:
        instruction = inputStream[programCounter]

        match instruction[0][0]:
            case 'c': # copy function
                if (instruction[1].isdecimal()):
                    registers[instruction[2]] = int(instruction[1])
                else:
                    registers[instruction[2]] = registers[instruction[1]]
                
            case 'i': # increment instruction
                registers[instruction[1]] += 1
            
            case 'd': # decrement instruction
                registers[instruction[1]] -= 1
            
            case 'j': # jump on not zero instruction
                if (instruction[1].isdecimal()):
                    if (int(instruction[1]) != 0):
                        programCounter += int(instruction[2])
                        continue

                else:
                    if (registers[instruction[1]] != 0):
                        programCounter += int(instruction[2])
                        continue
        
        programCounter += 1

    return registers

def taskOne(inputStream):
    registers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    }

    registers = executeProgram(registers)

    print(registers['a']) # 318117

def taskTwo(inputStream):
    registers = {
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0
    }

    registers = executeProgram(registers)
    
    print(registers['a']) # 9227771

taskOne(inputStream)
taskTwo(inputStream)

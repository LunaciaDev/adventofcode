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

    print(registers['a'])

def taskTwo(inputStream):
    registers = {
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0
    }

    registers = executeProgram(registers)
    
    print(registers['a'])

taskOne(inputStream)
taskTwo(inputStream)

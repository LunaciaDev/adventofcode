from copy import deepcopy

inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split("\n")

for inputStreamIndex in range(len(inputStream)):
    inputStream[inputStreamIndex] = inputStream[inputStreamIndex].split(" ")

def executeProgram(reg):
    registers = deepcopy(reg)
    instructionCount = len(inputStream)
    programCounter = 0
    output = None
    outputLength = 0

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

            case 'o':
                try:
                    outputVal = int(instruction[1])
                except:
                    outputVal = registers[instruction[1]]
                
                if (outputVal > 2 or outputVal < 0): return False
                if (output is None):
                    output = outputVal
                    outputLength += 1
                elif (output != outputVal):
                    output = outputVal
                    outputLength += 1
                else: return False

                if outputLength == 10:
                    return True

        programCounter += 1

    #just in case
    return True

def taskOne(inputStream):
    registers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    }

    while not executeProgram(registers):
        registers['a'] += 1
    
    print(registers['a'])

def taskTwo(inputStream):
    pass

taskOne(inputStream)
taskTwo(inputStream)

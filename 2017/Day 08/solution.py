inputFile = open("input")
inputStream = inputFile.read().strip().split("\n")

def catagorizeOperator(ops):
    total = 0
    for character in ops:
        total += ord(character)
    
    return total

for index in range(len(inputStream)):
    inputStream[index] = inputStream[index].split(" ")
    inputStream[index][5] = catagorizeOperator(inputStream[index][5])
    inputStream[index][2] = int(inputStream[index][2])
    inputStream[index][-1] = int(inputStream[index][-1])

def executeInstructions(instructions, defaultData):
    """
    condition: lvalue = #4, ops = #5, rvalue = #6
    ops: #1
    rvalue: #2
    lvalue: #0
    """
    registers = {'maxVal': 0}
    programCounter = 0

    while programCounter < len(instructions):
        instruction = instructions[programCounter]

        if registers.get(instruction[4], None) is None:
            registers[instruction[4]] = defaultData

        if registers.get(instruction[0], None) is None:
            registers[instruction[0]] = defaultData
        
        match(instruction[5]):
            case 62:
                if not registers[instruction[4]] > instruction[6]:
                    programCounter += 1
                    continue
            case 60:
                if not registers[instruction[4]] < instruction[6]:
                    programCounter += 1
                    continue
            case 94:
                if not registers[instruction[4]] != instruction[6]:
                    programCounter += 1
                    continue
            case 122:
                if not registers[instruction[4]] == instruction[6]:
                    programCounter += 1
                    continue
            case 121:
                if not registers[instruction[4]] <= instruction[6]:
                    programCounter += 1
                    continue
            case 123:
                if not registers[instruction[4]] >= instruction[6]:
                    programCounter += 1
                    continue

        match(instruction[1][0]):
            case 'i':
                registers[instruction[0]] += instruction[2]
            case 'd':
                registers[instruction[0]] -= instruction[2]

        if registers[instruction[0]] > registers['maxVal']:
            registers['maxVal'] = registers[instruction[0]]

        programCounter += 1
    
    return registers

def taskOne(inputStream):
    registers = executeInstructions(inputStream, 0)

    registers['maxVal'] = 0
    registerValues = sorted(list(registers.values()))

    print(registerValues[-1])

def taskTwo(inputStream):
    registers = executeInstructions(inputStream, 0)

    print(registers['maxVal'])

taskOne(inputStream)
taskTwo(inputStream)

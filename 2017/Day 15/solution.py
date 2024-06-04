inputFile = open("input")
inputStream = inputFile.read().strip().split("\n")

GENERATOR_SCALAR = [16807, 48271]
GENERATOR_MODULUS = 2147483647
GENERATOR_TARGET = [4, 8]

def taskOne(inputStream):
    first = int(inputStream[0].split()[-1])
    second = int(inputStream[1].split()[-1])
    matches = 0

    for _ in range(40000000):
        first = first * GENERATOR_SCALAR[0] % GENERATOR_MODULUS
        second = second * GENERATOR_SCALAR[1] % GENERATOR_MODULUS
        
        if first & 0xFFFF == second & 0xFFFF:
            matches += 1
    
    print(matches)

def taskTwo(inputStream):
    first = int(inputStream[0].split()[-1])
    second = int(inputStream[1].split()[-1])
    matches = 0

    for _ in range(5000000):
        while True:
            first = first * GENERATOR_SCALAR[0] % GENERATOR_MODULUS
            if first % 4 == 0: break
        
        while True:
            second = second * GENERATOR_SCALAR[1] % GENERATOR_MODULUS
            if second % 8 == 0: break

        if first & 0xFFFF == second & 0xFFFF:
            matches += 1
    
    print(matches)

taskOne(inputStream)
taskTwo(inputStream)

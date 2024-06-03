from math import floor

inputFile = open("input")
inputStream = inputFile.read().strip().split(',')

ROPE_SIZE = 256

def taskOne(inputStream):
    rope = list(range(ROPE_SIZE))
    skipSize = 0
    currPos = 0

    for length in inputStream:
        length = int(length)
        stepCount = floor(length / 2)
        
        # Doing reversal
        startPtr = currPos
        endPtr = (currPos + length) % ROPE_SIZE
        endPtr = ROPE_SIZE-1 if endPtr == 0 else endPtr - 1

        for _ in range(stepCount):
            temp = rope[startPtr]
            rope[startPtr] = rope[endPtr]
            rope[endPtr] = temp

            startPtr = (startPtr + 1) % ROPE_SIZE
            endPtr = ROPE_SIZE-1 if endPtr == 0 else endPtr - 1
        
        currPos = (currPos + skipSize + length) % ROPE_SIZE
        skipSize += 1
    
    print(rope[0] * rope[1])

"""
The requirement really went from 0 to 100 quick.
"""
def taskTwo(inputStream):
    dataStream = ",".join(inputStream)
    lengthArray = [ord(char) for char in dataStream] + [17, 31, 73, 47, 23]

    rope = list(range(ROPE_SIZE))
    skipSize = 0
    currPos = 0

    for _ in range(64):
        for length in lengthArray:
            stepCount = floor(length / 2)
            
            # Doing reversal
            startPtr = currPos
            endPtr = (currPos + length) % ROPE_SIZE
            endPtr = ROPE_SIZE-1 if endPtr == 0 else endPtr - 1

            for _ in range(stepCount):
                temp = rope[startPtr]
                rope[startPtr] = rope[endPtr]
                rope[endPtr] = temp

                startPtr = (startPtr + 1) % ROPE_SIZE
                endPtr = ROPE_SIZE-1 if endPtr == 0 else endPtr - 1
            
            currPos = (currPos + skipSize + length) % ROPE_SIZE
            skipSize += 1

    denseHash = []
    
    for offset in range(16):
        result = rope[16 * offset]
        for target in range(1, 16):
            result ^= rope[16 * offset + target]
        denseHash.append(hex(result)[2:].zfill(2))

    print("".join(denseHash))

#taskOne(inputStream)
taskTwo(inputStream)
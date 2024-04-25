from math import floor

inputFile = open("input")
inputStream = inputFile.read()

"""
This thing take minutes to run... prob at O(n^k) or smth
How would you get O(n)?
"""

def taskOne(inputStream):
    elvesCircle = [i+1 for i in range(int(inputStream))]

    while len(elvesCircle) > 1:
        removeFirstElf = False

        if len(elvesCircle) % 2 == 1: 
            removeFirstElf = True
            rangeObject = range(len(elvesCircle)-2, -1, -2)
        else:
            rangeObject = range(len(elvesCircle)-1, -1, -2)

        for elfIndex in rangeObject:
            elvesCircle.pop(elfIndex)
            
        if removeFirstElf: elvesCircle.pop(0)

    return elvesCircle[0]

def taskTwo(inputStream):
    elvesCircle = [i+1 for i in range(int(inputStream))]

    while len(elvesCircle) > 1:
        elfIndex = 0

        while elfIndex < len(elvesCircle):
            target = (floor(len(elvesCircle)/2) + elfIndex) % len(elvesCircle)
            elvesCircle.pop(target)

            if target <= elfIndex: continue
            elfIndex += 1 

    return elvesCircle[0]

print(taskOne(inputStream)) # 1842613
print(taskTwo(inputStream)) # 1424135
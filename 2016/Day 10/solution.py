inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")

botProgramming = {}
outputBins = {}
processingQueue = []

def programBots(inputStream):
    for instruction in inputStream:
        if instruction[0] == "b": # bot programming instruction
            instruction = instruction.split(" ")

            if botProgramming.get(int(instruction[1]), None) is not None:
                currentBot = botProgramming[int(instruction[1])]
                currentBot["lo"] = int(instruction[6])
                currentBot["loOutput"] = instruction[5][0] == 'o'
                currentBot["hi"] = int(instruction[11])
                currentBot["hiOutput"] = instruction[10][0] == 'o'
            
            else:
                botProgramming[int(instruction[1])] = {
                    "lo": int(instruction[6]),
                    "loOutput": instruction[5][0] == 'o',
                    "hi": int(instruction[11]),
                    "hiOutput": instruction[10][0] == 'o',
                    "currentChips": [],
                    "chipsCount": 0
                }

            if instruction[5][0] == 'o':
                outputBins[int(instruction[6])] = {
                    "currentChip": 0
                }

            if instruction[10][0] == 'o':
                outputBins[int(instruction[11])] = {
                    "currentChip": 0
                }

        else: # bot have chips instruction
            instruction = instruction.split(" ")
            if botProgramming.get(int(instruction[5]), None) is not None:
                currentBot = botProgramming[int(instruction[5])]
                currentBot["currentChips"].append(int(instruction[1]))
                
                if currentBot["chipsCount"] == 1:
                    processingQueue.append(int(instruction[5]))
                
                currentBot["chipsCount"] += 1

            else:
                botProgramming[int(instruction[5])] = {
                    "lo": -1,
                    "loOutput": False,
                    "hi": -1,
                    "hiOutput": False,
                    "currentChips": [int(instruction[1])],
                    "chipsCount": 1
                }

def executeInstruction():
    while len(processingQueue) != 0:
        currentBot = botProgramming[processingQueue.pop(0)]
        currentBot["currentChips"].sort()

        currentChip = currentBot["currentChips"][0]

        if currentBot["loOutput"]:
            outputBins[currentBot["lo"]] = currentChip
        
        else:
            targetBot = botProgramming[currentBot["lo"]]

            targetBot["currentChips"].append(currentChip)
            
            if targetBot["chipsCount"] == 1:
                processingQueue.append(currentBot["lo"])
            
            targetBot["chipsCount"] += 1
        
        currentChip = currentBot["currentChips"][1]

        if currentBot["hiOutput"]:
            outputBins[currentBot["hi"]] = currentChip
        
        else:
            targetBot = botProgramming[currentBot["hi"]]

            targetBot["currentChips"].append(currentChip)
            
            if targetBot["chipsCount"] == 1:
                processingQueue.append(currentBot["hi"])
            
            targetBot["chipsCount"] += 1
        
        currentBot["chipsCount"] = 0

programBots(inputStream)
executeInstruction()

def taskOne():
    for botID in botProgramming:
        bot = botProgramming[botID]
        if bot["currentChips"][0] == 17 and bot["currentChips"][1] == 61:
            print(botID)
            return

def taskTwo():
    print(outputBins[0]
          * outputBins[1]
          * outputBins[2]
        )

taskOne()
taskTwo()

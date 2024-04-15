inputFile = open("input")
inputStream = inputFile.read()

reindeerSpeed = []

#Sanitizing input
inputStream = inputStream.split("\n")
for line in inputStream:
    line = line.split(" ")
    reindeerSpeed.append([int(line[3]), int(line[6]), int(line[-2])])

def taskOne(inputStream):
    maxDist = 0
    for reindeer in reindeerSpeed:
        reindeerDist = ( 2503 // (reindeer[1] + reindeer[2]) ) * ( reindeer[0] * reindeer[1] )
        timeLeft = 2503 % (reindeer[1] + reindeer[2])

        if timeLeft > reindeer[1]:
            reindeerDist += reindeer[0] * reindeer[1]
        else:
            reindeerDist += reindeer[0] * timeLeft

        if reindeerDist > maxDist:
            maxDist = reindeerDist
    
    print(maxDist) #2640

def taskTwo(inputStream):
    reindeerDist = [0 for i in range(9)]
    reindeerPoint = [0 for i in range(9)]
    reindeerRunTime = [reindeerSpeed[i][1] for i in range(9)]
    reindeerRestTime = [0 for i in range(9)]

    for _ in range(2503): #Man
        maxDist = 0
        reindeerMaxDist = []
        for index in range(9):
            if reindeerRunTime[index] > 0:
                if reindeerRunTime[index] == 1:
                    reindeerRestTime[index] = reindeerSpeed[index][2]

                reindeerRunTime[index] -= 1
                reindeerDist[index] += reindeerSpeed[index][0]

                if reindeerDist[index] > maxDist:
                    maxDist = reindeerDist[index]
                    reindeerMaxDist = [index]
                    continue

                if reindeerDist[index] == maxDist:
                    reindeerMaxDist.append(index)
                    continue

                continue

            if reindeerRestTime[index] > 0:
                if reindeerRestTime[index] == 1:
                    reindeerRunTime[index] = reindeerSpeed[index][1]
                
                reindeerRestTime[index] -= 1

                if reindeerDist[index] > maxDist:
                    maxDist = reindeerDist[index]
                    reindeerMaxDist = [index]
                    continue

                if reindeerDist[index] == maxDist:
                    reindeerMaxDist.append(index)
                    continue

                continue
        
        for reindeer in reindeerMaxDist:
            reindeerPoint[reindeer] += 1
    
    reindeerPoint.sort()
    print(reindeerPoint[-1]) #1102
        
taskOne(inputStream)
taskTwo(inputStream)
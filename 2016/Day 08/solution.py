inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")
screen = [[0 for _ in range(50)] for _ in range(6)]

def taskOne(inputStream):
    for instruction in inputStream:
        instruction = instruction.split(" ")

        if instruction[0][1] == "e": # rect instruction
            instruction = instruction[1].split("x")

            for i in range(int(instruction[1])):
                for k in range(int(instruction[0])):
                    screen[i][k] = 1

        else: # rotate instruction
            if instruction[1][0] == "r": # rotate row
                rowID = int(instruction[2].split("=")[1])
                rotateAmount = int(instruction[4])

                newRow = [0 for _ in range(50)]

                for i in range(50):
                    if screen[rowID][i] == 0: continue

                    newIndex = i + rotateAmount

                    if newIndex >= 50: 
                        newIndex -= 50

                    newRow[newIndex] = 1
                
                for i in range(50):
                    screen[rowID][i] = newRow[i]

            else: # rotate column
                colID = int(instruction[2].split("=")[1])
                rotateAmount = int(instruction[4])

                newCol = [0 for _ in range(6)]

                for i in range(6):
                    if screen[i][colID] == 0: continue

                    newIndex = i + rotateAmount

                    if newIndex >= 6: 
                        newIndex -= 6

                    newCol[newIndex] = 1
                
                for i in range(6):
                    screen[i][colID] = newCol[i]

    voltageUsage = sum([sum(screen[i]) for i in range(6)])
    print(voltageUsage)

def taskTwo(inputStream):
    for i in range(len(screen)):
        for k in range(len(screen[i])):
            print("#", end="") if screen[i][k] == 1 else print(".", end="")
        
        print("")

    """
    ####.####.#..#.####..###.####..##...##..###...##..
    ...#.#....#..#.#....#....#....#..#.#..#.#..#.#..#.
    ..#..###..####.###..#....###..#..#.#....#..#.#..#.
    .#...#....#..#.#.....##..#....#..#.#.##.###..#..#.
    #....#....#..#.#.......#.#....#..#.#..#.#....#..#.
    ####.#....#..#.#....###..#.....##...###.#.....##..
    """

taskOne(inputStream)
taskTwo(inputStream)

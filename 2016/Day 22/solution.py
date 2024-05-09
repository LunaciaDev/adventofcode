inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split("\n")
inputStream = inputStream[2:]

def taskOne(inputStream):
    nodeArray = []
    counter = 0

    for node in inputStream:
        node = node.split(" ")
        node = [i for i in node if i != '']

        nodeArray.append((int(node[2][:-1]), int(node[3][:-1])))

    for indexA in range(len(nodeArray)):
        if nodeArray[indexA][0] == 0: continue
        for indexB in range(len(nodeArray)):
            if indexA == indexB: continue

            if nodeArray[indexA][0] <= nodeArray[indexB][1]:
                counter += 1

    print(counter)

def taskTwo(inputStream):
    dim = (38, 28)
    nodeArray = []
    
    for node in inputStream:
        node = node.split(" ")
        node = [i for i in node if i != '']

        nodeArray.append((int(node[1][:-1]), int(node[2][:-1]), int(node[3][:-1])))

    for y in range(dim[1]):
        for x in range(dim[0]):
            targetNode = nodeArray[x * dim[1] + y]
            if (targetNode[0] > 99 or targetNode[1] > 85):
                print("||/||", end=" ")
            elif (targetNode[1] == 0): 
                print("_____", end= " ")
            else:
                print(str(targetNode[1]).zfill(2) + "/" + str(targetNode[0]).zfill(2), end=" ")
        
        print()

    # Solving it by hand, yield 272
    # Move the empty node to the top right corner of the grid
    # Then move the target data (top right-1) to the top left, each movement of the target cost 5 moves :D


taskOne(inputStream) # 1038
taskTwo(inputStream)

from collections import deque

inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.strip().split("\n")

for index in range(len(inputStream)):
    inputStream[index] = inputStream[index].strip().split(" <-> ")
    inputStream[index].pop(0)
    inputStream[index] = inputStream[index][0].split(", ")
    
    for nodeIndex in range(len(inputStream[index])):
        inputStream[index][nodeIndex] = int(inputStream[index][nodeIndex])

"""
The problem can be rephrased as "Find maximal simple path in the graph containing node 0"
then we return the number of vertices in that path
BFS away!
"""
def taskOne(adjacencyList):
    visited = [False for _ in range(len(adjacencyList))]
    visited[0] = True
    spanningTreeSize = 1
    nodeQueue = deque()
    nodeQueue.append(0)

    while len(nodeQueue) > 0:
        currentNode = nodeQueue.popleft()

        for connectedNode in adjacencyList[currentNode]:
            if visited[connectedNode]: continue
            
            nodeQueue.append(connectedNode)
            visited[connectedNode] = True
            spanningTreeSize += 1
    
    print(spanningTreeSize)

"""
Recycle the first part but this time we find how many connected components are there
should be simple enough
"""
def taskTwo(adjacencyList):
    visited = [False for _ in range(len(adjacencyList))]
    visitedCount = 0
    pathCount = 0
    nodeQueue = deque()

    while visitedCount < len(adjacencyList):
        pathCount += 1

        for nodeIndex in range(len(visited)):
            if not visited[nodeIndex]:
                nodeQueue.append(nodeIndex)
                visitedCount += 1
                visited[nodeIndex] = True
                break

        while len(nodeQueue) > 0:
            currentNode = nodeQueue.popleft()

            for connectedNode in adjacencyList[currentNode]:
                if visited[connectedNode]: continue
                
                nodeQueue.append(connectedNode)
                visited[connectedNode] = True
                visitedCount += 1

    print(pathCount)

taskOne(inputStream)
taskTwo(inputStream)

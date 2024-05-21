from copy import deepcopy

inputFile = open("input")
inputStream = inputFile.read()
inputStream = inputStream.strip().split('\n')

class TreeNode:
    name = None
    parent = None
    child = None
    value = None
    sumSubtreeValue = 0

    def setName(self, name):
        self.name = name

    def setParent(self, parent):
        self.parent = parent

    def setChilds(self, childs):
        self.child = deepcopy(childs)
    
    def setValue(self, value):
        self.value = value

    def setSumSubtreeValue(self, value):
        self.sumSubtreeValue = value
    
    def getParent(self):
        return self.parent
    
    def getValue(self):
        return self.value
    
    def getChild(self):
        return self.child
    
    def getName(self):
        return self.name
    
    def getSumSubtreeValue(self):
        return self.sumSubtreeValue

nodeCollection = {}
rootNode = None

def taskOne(inputStream):
    global rootNode
    for node in inputStream:
        node = node.split(" ")
        
        if nodeCollection.get(node[0], None) is None:
            nodeCollection[node[0]] = TreeNode()
            nodeCollection[node[0]].setName(node[0])

        nodeCollection[node[0]].setValue(int(node[1][1:-1]))

        if (len(node) > 2):
            nodeChilds = []
            for childNode in node[3:]:
                if childNode[-1] == ',':
                    target = childNode[:-1]
                else:
                    target = childNode

                if nodeCollection.get(target, None) is None:
                    nodeCollection[target] = TreeNode()
                    nodeCollection[target].setName(target)

                nodeCollection[target].setParent(nodeCollection[node[0]])
                nodeChilds.append(target)
        else:
            nodeChilds = None
        
        nodeCollection[node[0]].setChilds(nodeChilds)

    currentNode = nodeCollection[list(nodeCollection.keys())[0]]

    while currentNode.getParent() is not None:
        currentNode = currentNode.getParent()
    
    print(currentNode.getName())
    rootNode = currentNode

def balanceSubtree(currentNode):
    childList = currentNode.getChild()

    if childList is None: return False

    subtreeValues = {}

    for children in childList:
        children = nodeCollection[children]

        foundImbalance = balanceSubtree(children)
        if foundImbalance:
            return True

        temp = children.getSumSubtreeValue() + children.getValue()

        if subtreeValues.get(temp, None) is None:
            subtreeValues[temp] = 1
        else:
            subtreeValues[temp] += 1

    if len(list(subtreeValues.keys())) > 1:
        possibleValues = list(subtreeValues.keys())
        oddValue = possibleValues[0]
        normalValue = possibleValues[1]

        if subtreeValues[possibleValues[1]] == 1:
            oddValue = possibleValues[1]
            normalValue = possibleValues[0]
        
        for children in childList:
            children = nodeCollection[children]
            if children.getSumSubtreeValue() + children.getValue() == oddValue:
                print(children.getValue() + (normalValue - oddValue))
                break

        return True

    currentNode.setSumSubtreeValue(list(subtreeValues.keys())[0] * len(childList))
    return False

def taskTwo(inputStream):
    balanceSubtree(rootNode)

taskOne(inputStream)
taskTwo(inputStream)
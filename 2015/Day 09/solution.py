import copy

inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")

def construcPathTable(inputStream):
    pathTable = [[0 for _ in range(8)] for _ in range(8)]
    locationLookup = {}
    locationId = 0
    for path in inputStream:
        path = path.split()
        if locationLookup.get(path[0], None) == None:
            locationLookup[path[0]] = locationId
            locationId += 1
        if locationLookup.get(path[2], None) == None:
            locationLookup[path[2]] = locationId
            locationId += 1

        pathTable[locationLookup[path[0]]][locationLookup[path[2]]] = int(path[-1])
        pathTable[locationLookup[path[2]]][locationLookup[path[0]]] = int(path[-1])

    return pathTable

pathTable = construcPathTable(inputStream)

def taskOne(pathTable):
    #Since there's no fixed start/end, smell like a brute force problem
    def solver(unvisitedCities, currentDist, currentCity):
        minDistance = 100000 
        if unvisitedCities == []:
            return currentDist
            
        for target in unvisitedCities:
            nextUnvisitedList = copy.copy(unvisitedCities)
            nextUnvisitedList.remove(target)
            tempDist = solver(nextUnvisitedList, currentDist + pathTable[currentCity][target], target)
            
            if tempDist < minDistance:
                minDistance = tempDist
        
        return minDistance
    
    minDistance = 100000 
    for city in range(8):
        cityList = [i for i in range(8)]
        cityList.remove(city)
        tempDist = solver(cityList, 0, city)
        if tempDist < minDistance:
            minDistance = tempDist

    print(minDistance)

def taskTwo(pathTable):
    def solver(unvisitedCities, currentDist, currentCity):
        maxDistance = 0 
        if unvisitedCities == []:
            return currentDist
            
        for target in unvisitedCities:
            nextUnvisitedList = copy.copy(unvisitedCities)
            nextUnvisitedList.remove(target)
            tempDist = solver(nextUnvisitedList, currentDist + pathTable[currentCity][target], target)
            
            if tempDist > maxDistance:
                maxDistance = tempDist
        
        return maxDistance
    
    maxDistance = 0
    for city in range(8):
        cityList = [i for i in range(8)]
        cityList.remove(city)
        tempDist = solver(cityList, 0, city)
        if tempDist > maxDistance:
            maxDistance = tempDist

    print(maxDistance)

taskOne(pathTable)
taskTwo(pathTable)

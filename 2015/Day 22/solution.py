import copy

inputFile = open("input")
inputStream = inputFile.read()

inputStream = inputStream.split("\n") 

playerActions = {
    "MagicMissles": {
        "ManaCost": 53,
        "Damage": 4
    },
    "Drain": {
        "ManaCost": 73,
        "Damage": 2,
        "Heal": 2
    },
    "Shield": {
        "ManaCost": 113,
        "Effect": {
            "Armor": 7,
            "Duration": 6
        }
    },
    "Poison": {
        "ManaCost": 173,
        "Effect": {
            "Damage": 3,
            "Duration": 6
        }
    },
    "Recharge": {
        "ManaCost": 229,
        "Effect": {
            "Mana": 101,
            "Duration": 5
        }
    }
}

effectTrans = {
    "Armor": 0,
    "Damage": 1,
    "Mana": 2
}

def taskOne(inputStream):
    bossStat = []

    for line in inputStream:
        line = line.split(" ")
        bossStat.append(int(line[-1]))

    playerHP = 50
    playerMana = 500

    def combatSim(currentHP, currentMana, currentBossHP, manaSpent, effectList, whoseTurn):
        minManaSpent = 10000000
        
        #Trimming the search tree
        if manaSpent > 1000:
            return minManaSpent

        #Looping through effects
        playerArmor = 7 if effectList[0] > 1 else 0
        currentBossHP -= 3 if effectList[1] > 0 else 0
        currentMana += 101 if effectList[2] > 0 else 0

        for effectIndex in range(len(effectList)):
            if effectList[effectIndex] > 0:
                effectList[effectIndex] -= 1
        
        if currentBossHP <= 0:
            return manaSpent

        #Boss' turn
        if whoseTurn == 1:
            whoseTurn = 0

            if currentHP - (8 - playerArmor) <= 0:
                return minManaSpent
        
            currentHP -= 8 - playerArmor
            newEffectList = copy.copy(effectList)

            tempManaSpent = combatSim(currentHP, currentMana, currentBossHP, manaSpent, newEffectList, whoseTurn)
            
            if tempManaSpent < minManaSpent:
                minManaSpent = tempManaSpent
            
            return minManaSpent
            
        #Player's turn
        #Looping through attacks
        whoseTurn = 1
        for action in playerActions:
            action = playerActions[action]

            if action["ManaCost"] > currentMana: continue
            
            if action.get("Effect", None) != None:
                effect = list(action.get("Effect").keys())
                
                newEffectList = copy.copy(effectList)
                if newEffectList[effectTrans[effect[0]]] != 0: continue

                newEffectList[effectTrans[effect[0]]] = action["Effect"]["Duration"]
                
                tempManaSpent = combatSim(currentHP, currentMana - action["ManaCost"], currentBossHP, 
                                          manaSpent + action["ManaCost"], newEffectList, whoseTurn)
            
            else:
                newEffectList = copy.copy(effectList)
                tempManaSpent = combatSim(currentHP + action.get("Heal", 0), currentMana - action["ManaCost"], 
                                          currentBossHP - action["Damage"], manaSpent + action["ManaCost"], newEffectList, whoseTurn)   

            if tempManaSpent < minManaSpent:
                minManaSpent = tempManaSpent
        
        return minManaSpent

    print(combatSim(playerHP, playerMana, bossStat[0], 0, [0, 0, 0], 0)) #953

def taskTwo(inputStream):
    bossStat = []

    for line in inputStream:
        line = line.split(" ")
        bossStat.append(int(line[-1]))

    playerHP = 50
    playerMana = 500

    def combatSim(currentHP, currentMana, currentBossHP, manaSpent, effectList, whoseTurn):
        minManaSpent = 10000000
        
        #Trimming the search tree
        if manaSpent > 1500:
            return minManaSpent

        #Looping through effects
        playerArmor = 7 if effectList[0] > 1 else 0
        currentBossHP -= 3 if effectList[1] > 0 else 0
        currentMana += 101 if effectList[2] > 0 else 0
        currentHP -= 1 if whoseTurn == 0 else 0

        for effectIndex in range(len(effectList)):
            if effectList[effectIndex] > 0:
                effectList[effectIndex] -= 1
        
        if currentHP <= 0:
            return minManaSpent

        if currentBossHP <= 0:
            return manaSpent

        #Boss' turn
        if whoseTurn == 1:
            whoseTurn = 0

            if currentHP - (8 - playerArmor) <= 0:
                return minManaSpent
        
            currentHP -= 8 - playerArmor
            newEffectList = copy.copy(effectList)

            tempManaSpent = combatSim(currentHP, currentMana, currentBossHP, manaSpent, newEffectList, whoseTurn)
            
            if tempManaSpent < minManaSpent:
                minManaSpent = tempManaSpent
            
            return minManaSpent
            
        #Player's turn
        #Looping through attacks
        whoseTurn = 1
        for action in playerActions:
            action = playerActions[action]

            if action["ManaCost"] > currentMana: continue
            
            if action.get("Effect", None) != None:
                effect = list(action.get("Effect").keys())
                
                newEffectList = copy.copy(effectList)
                if newEffectList[effectTrans[effect[0]]] != 0: continue

                newEffectList[effectTrans[effect[0]]] = action["Effect"]["Duration"]
                
                tempManaSpent = combatSim(currentHP, currentMana - action["ManaCost"], currentBossHP, 
                                          manaSpent + action["ManaCost"], newEffectList, whoseTurn)
            
            else:
                newEffectList = copy.copy(effectList)
                tempManaSpent = combatSim(currentHP + action.get("Heal", 0), currentMana - action["ManaCost"], 
                                          currentBossHP - action["Damage"], manaSpent + action["ManaCost"], newEffectList, whoseTurn)   

            if tempManaSpent < minManaSpent:
                minManaSpent = tempManaSpent
        
        return minManaSpent

    print(combatSim(playerHP, playerMana, bossStat[0], 0, [0, 0, 0], 0)) #1289


taskOne(inputStream)
taskTwo(inputStream)
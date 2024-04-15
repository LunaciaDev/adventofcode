import math
import itertools

inputFile = open("input")
inputStream = inputFile.read()

#Sanitizing input
inputStream = inputStream.split("\n")
bossStats = []
for line in inputStream:
    line = line.split(" ")
    bossStats.append(int(line[-1]))

weaponCost = [8, 10, 25, 40, 74]
armorCost = [0, 13, 31, 53, 75, 102]
damageRing = [0, 25, 50, 100]
armorRing = [0, 20, 40, 80]

'''
Funni bruteforce go brrrrrrr
taskOne could be solved by greedy - only armor ring as damage ring are scam 
(I actually solved it by hand) but it's a mess writing it as code
taskTwo... yea.
'''

def taskOne():
    leastGoldCost = 1000000

    for damage in range(len(weaponCost)):
        for armor in range(len(armorCost)):
            goldCost = weaponCost[damage] + armorCost[armor]
            for ringCombination in itertools.combinations("01234567", 2):
                ringCost = 0
                ringDamage = 0
                ringArmor = 0
                for ring in ringCombination:
                    ring = int(ring)

                    if ring > 3:
                        ringArmor += ring - 4
                        ringCost += armorRing[ring-4]
                        continue
                    
                    ringDamage += ring
                    ringCost += damageRing[ring]

                if math.ceil(bossStats[0]/max((damage + ringDamage + 4 - bossStats[2]), 1)) < math.ceil(100/max((bossStats[1] - armor - ringArmor), 1)):
                    if goldCost + ringCost < leastGoldCost:    
                        leastGoldCost = goldCost + ringCost

    print(leastGoldCost) #111

def taskTwo():
    mostGoldCost = 0

    for damage in range(len(weaponCost)):
        for armor in range(len(armorCost)):
            goldCost = weaponCost[damage] + armorCost[armor]
            for ringCombination in itertools.combinations("01234567", 2):
                ringCost = 0
                ringDamage = 0
                ringArmor = 0
                for ring in ringCombination:
                    ring = int(ring)

                    if ring > 3:
                        ringArmor += ring - 4
                        ringCost += armorRing[ring-4]
                        continue
                    
                    ringDamage += ring
                    ringCost += damageRing[ring]

                if math.ceil(bossStats[0]/max((damage + ringDamage + 4 - bossStats[2]), 1)) >= math.ceil(100/max((bossStats[1] - armor - ringArmor), 1)):
                    if goldCost + ringCost > mostGoldCost:    
                        mostGoldCost = goldCost + ringCost

    print(mostGoldCost) #188

taskOne()
taskTwo()
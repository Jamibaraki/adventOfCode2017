#Spiral Memory
#Advent of Code 2017 Day 3

#doesn't work for value: 1


import math


def checkTarget():
    if currentCount == target:
        answer = math.fabs(xPos) + math.fabs(yPos)
        print("Answer: " + str(answer))
        exit
        return 1
    return 0



rBound = 0
lBound = 0
uBound = 0
dBound = 0


xPos = 0
yPos = 0

currentCount = 1
target = 289326

while currentCount <= target:
    #move right until we exceed rightbound
    while xPos<=rBound:
        xPos += 1
        currentCount += 1
        checkTarget()
    rBound = xPos
    #move up until we exceed upbount
    while yPos>=uBound:
        yPos -= 1
        currentCount += 1
        checkTarget()
    uBound = yPos
    #move left until we exceed leftbound
    while xPos>= lBound:
        xPos -= 1
        currentCount += 1
        checkTarget()
    lBound = xPos
    #move down until we exceed downbound
    while yPos <= dBound:
        yPos += 1
        currentCount += 1
        checkTarget()
    dBound = yPos

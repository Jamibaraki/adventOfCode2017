#Spiral Memory
#Advent of Code 2017 Day 3b

#First printed value is right answer


import math



def calculateSpace():
    #startX = xPos-1
    #startY = yPos-1
    score = 0
    for x in range ( xPos-1,xPos+2 ):
        for y in range( yPos-1,yPos+2):
            if  ( str(x)+"."+str(y) ) in values:
                score += values[str(x)+"."+str(y)]
    values[ str(xPos)+"."+str(yPos) ] = score
    if score > target:
        print( "finished: " + str(score) )
        finished = True
        return True
    return False



rBound = 0
lBound = 0
uBound = 0
dBound = 0


xPos = 0
yPos = 0

currentCount = 1
target = 289326
values = {'0.0' : 1 }
finished = False

while finished == False:
    #move right until we exceed rightbound
    while xPos<=rBound:
        xPos += 1
        currentCount += 1
        if calculateSpace():
            finished = True
            exit
        #checkTarget()
    rBound = xPos
    #move up until we exceed upbount
    while yPos>=uBound:
        yPos -= 1
        currentCount += 1
        if calculateSpace():
            finished = True
            exit
        #checkTarget()
    uBound = yPos
    #move left until we exceed leftbound
    while xPos>= lBound:
        xPos -= 1
        currentCount += 1
        if calculateSpace():
            finished = True
            exit
        #checkTarget()
    lBound = xPos
    #move down until we exceed downbound
    while yPos <= dBound:
        yPos += 1
        currentCount += 1
        if calculateSpace():
            finished = True
            exit
        #checkTarget()
    dBound = yPos

#Advent of Code 22a
# Sporifica Virus

#import numpy as np


import time
start_time = time.time()
print('Fractal Art')
#file = open('inputTest.txt','r')
file = open('input22.txt','r')
input = file.read().split('\n')
file.close()


print(input)   

#pattern = []
#for line in input:
    
#pattern.append('..#')
#pattern.append('#..')
#pattern.append('...')

directions = ['UP','RIGHT','DOWN','LEFT']
directionIndex = 0 #start heading up

infectedNodes = []
for yPos in range( 0, len(input) ):
    for xPos in range( 0, len(input) ):
        if input[yPos][xPos] == '#':
            infectedNodes.append( [xPos,yPos] )

print(len(infectedNodes) )
print( infectedNodes)

def detectInfected( inputX, inputY ):
    for node in infectedNodes:
        if node == [inputX,inputY]:
            return True
    return False

def removeInfected( inputX, inputY ):
    for node in infectedNodes:
        if node == [inputX,inputY]:
            #print('found the node to remove')
            infectedNodes.remove(node)
            return

def turnLeft():
    global directionIndex
    directionIndex -= 1
    if directionIndex < 0:
        directionIndex = 3

def turnRight():
    global directionIndex
    directionIndex +=1
    if directionIndex > 3:
        directionIndex = 0

#test for sample input
def test():
    #check positive detection
    if detectInfected( 2,0 ) and detectInfected( 0,1 ):
        pass
    else:
        print('detectInfected failed')
        return False

    if detectInfected( 0,0) or detectInfected( 2,1 ) or detectInfected(2,2):
        print('detectInfected false positive')
        return False

    return True

xPos = 12
yPos = 12

#occurances of infectinos
infections = 0

bursts = 10000
for x in range(0,bursts):
    #if we are on an infected node disinfect and turn right.
    if detectInfected( xPos, yPos ):
        removeInfected( xPos, yPos )
        turnRight()
    #if we are on a disinfected node, infect and turn left.
    else:
        infectedNodes.append( [xPos,yPos] )
        infections += 1
        turnLeft()
        
    #move forward
    direction = directions[directionIndex]
    if direction == 'UP':
        #print('moving up')
        yPos -= 1
    elif direction == 'LEFT':
        #print('moving left')
        xPos -= 1
    elif direction == 'DOWN':
        #print('moving down')
        yPos += 1
    elif direction == 'RIGHT':
        #print('moving right')
        xPos += 1

    #print( 'New Position: ' + str(xPos) + ' ' + str(yPos) )


#print( 'Test results = ' + str( test() ) )

print(time.time() - start_time )

print( 'Burts : ' + str(bursts) )

print( 'infection count: ' + str( len( infectedNodes ) ) )
print( 'occurences of infection: ' + str( infections ) )
#print( infectedNodes )
print( xPos ,yPos )





      
    
    





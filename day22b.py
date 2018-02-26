#Advent of Code 22b
# Sporifica Virus

#import numpy as np


import time
start_time = time.time()
print('Sporifica test')
#file = open('inputTest.txt','r')
file = open('input22.txt','r')
input = file.read().split('\n')
file.close()


#print(input)   

#pattern = []
#for line in input:
    
#pattern.append('..#')
#pattern.append('#..')
#pattern.append('...')

#directions = ['UP','RIGHT','DOWN','LEFT']
#directions = [0,1,2,3]
directionIndex = 0 #start heading up


weakenedNodes = {}

flaggedNodes = {}

infectedNodes = {}

for yPos in range( 0, len(input) ):
    for xPos in range( 0, len(input) ):
        if input[yPos][xPos] == '#':
            infectedNodes[ str(xPos)+'.'+str(yPos) ] = 1 
            

#print(len(infectedNodes) )
#print( infectedNodes)

def detectInfected( inputX, inputY ):
    #if [inputX,inputY] in infectedNodes:
    #    infectedNodes.remove([inputX,inputY])
    if str(xPos)+'.'+str(yPos) in infectedNodes:
        del infectedNodes[ str(xPos)+'.'+str(yPos) ]
        return True
    return False
##    for node in infectedNodes:
##        if node == [inputX,inputY]:
##            return True
##    return False

def detectFlagged( inputX, inputY ):
    if str(xPos)+'.'+str(yPos) in flaggedNodes:
        #flaggedNodes.remove([inputX,inputY])
        del flaggedNodes[ str(xPos)+'.'+str(yPos) ]
        return True
    return False
##    for node in flaggedNodes:
##        if node == [inputX,inputY]:
##            return True
##    return False

def detectWeakened( inputX, inputY ):
    if str(xPos)+'.'+str(yPos) in weakenedNodes:
    #if [inputX,inputY ] in weakenedNodes:
        #weakenedNodes.remove([inputX,inputY])
        del weakenedNodes[ str(xPos)+'.'+str(yPos) ]
        return True
    return False
##    for node in weakenedNodes:
##        if node == [inputX,inputY]:
##            return True
##    return False


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

xPos = 12 #12
yPos = 12 #12 

#occurances of infectinos
infections = 0

bursts = 10000000
#bursts = 100000 #4.836/5  0.24
#bursts = 10000 #0.09 #0.024

ticks = 0
tick = 0
tickLimit = 100000

for x in range(0,bursts):

    tick +=1
    if tick == tickLimit:
        ticks +=1
        tick = 0
        print( "tick: " + str(ticks) )
    
    #if we are on an infected node flag and turn right.
    if detectInfected( xPos, yPos ):
        #removeInfected( xPos, yPos )
        #flaggedNodes.append( [xPos, yPos] )
        flaggedNodes[ str(xPos)+'.'+str(yPos) ] = 1 
        turnRight()
    #if we are on a weakened node, infect it and keep moving
    elif detectWeakened( xPos, yPos ):
        #removeWeakened( xPos, yPos )
        #infectedNodes.append( [xPos, yPos] )
        infectedNodes[ str(xPos)+'.'+str(yPos) ] = 1 
        infections+=1

    #if we are on a flagged node, clean it and reverse direction
    elif detectFlagged( xPos, yPos ):
        #removeFlagged( xPos, yPos )
        turnLeft()
        turnLeft()
    #if we are on a clean node, weaken and turn left.
    else:
        weakenedNodes[ str(xPos)+'.'+str(yPos) ] = 1
        #infections += 1
        turnLeft()
        
    #move forward
    #direction = directions[directionIndex]
    
    if directionIndex == 0:
        #print('moving up')
        yPos -= 1
    elif directionIndex == 3:
        #print('moving left')
        xPos -= 1
    elif directionIndex == 2:
        #print('moving down')
        yPos += 1
    elif directionIndex == 1:
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





      
    
    





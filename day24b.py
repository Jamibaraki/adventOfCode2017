#Advent of Code 24b
# ElectroMagnetic Moat part 2
print('electromagnetic moat')


import time
start_time = time.time()

#file = open('inputTest.txt','r')
file = open('input24.txt','r')
input = file.read().split('\n')
file.close()

#for line in input:
for x in range( 0, len(input) ):
    input[x] = input[x].split('/')
    for y in range( 0, len(input[x] ) ):
        input[x][y] = int( input[x][y] )

print( input )

firstConnection = 0 #since bridge starts from 0

bridges = []

topScore = 0
maxLength = 0

def checkScore( currentList ):
    global topScore, maxLength
    score = 0
    length = len(currentList)
    if length >= maxLength:
        maxLength = length
        for item in currentList:
            block = input[item]
            score += block[0]
            score += block[1]
        if score > topScore:
            topScore = score
            return True
    return False
    
        

def buildBridge( currentList, nextConnection ):
    #find a block that connects and isn't in the current bridge
    #print('buildbridge' + str( currentList ) )
    nextSteps = []
    #for block in input:
    for x in range(0,len(input)):
        block = input[x]
        if block[0] == nextConnection or block[1] == nextConnection:
            if x not in currentList:
                #nextSteps.append( block )
                nextSteps.append( x )
            #print('found one' + str( block  ) )
            
    nextValue = 0
    #go through the blocks recursively
    for step in nextSteps:
        #newList = currentList.append( step )
        newList = currentList[:]
        newList.append( step )
        block = input[step]
        if block[0] == nextConnection:
            buildBridge( newList, block[1] )
        else:
            buildBridge( newList, block[0] )
        
    #if there isn't one, return
    #print( currentList )
    checkScore( currentList )
    return

currentBridge = []
buildBridge( currentBridge, firstConnection )
print( topScore )

#Advent of Code '17
#Day 12b: Digital Plumber


import re


#read input
file = open('input12.txt','r')
input = file.read().split('\n')
file.close()

#list of which we have found to be connected
connected = []



for x in range(0, len(input)):
        input[x] = input[x].split(' ')
        connected.append( False )
        

def checkGroup( startPosition ):
        totalConnections = 0
        toAdd = []
        toAdd.append(startPosition)
        while( len(toAdd) ):
                nextLine = toAdd.pop()
                if connected[nextLine] == False:
                        connected[nextLine] = True
                        totalConnections += 1
                        for value in range( 2, len(input[nextLine]) ):
                                number = re.sub("[^0-9]","",input[nextLine][value])
                                toAdd.append( int(number) )


#checkGroup( 0 )


#find the next unconnected node
def findUnconnected():
        for x in range(0,len(input) ):
                if connected[x] == False:
                        return x
        return -1

totalGroups = 0

nextStart = findUnconnected()

while nextStart != -1:
        checkGroup( nextStart )
        totalGroups += 1
        nextStart = findUnconnected()
                    
print( "TotalGroups: " + str(totalGroups) )




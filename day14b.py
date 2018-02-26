#Advent of Code '17
#Day 14b - Disk Defragmentation, hunting for regions

#store results in grid
#hunt for 1 in grid
#find any adjascent and add to list
        #keep searching new ones for further additions
#when done, set region to zeros, inc result counter and repeat until we don't find any ones

import binascii

def knotHash( value ):
        elements = []
        for x in range( 0,256):
                elements.append( x )

        #inputlengths = [76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229]
        inputlengths = value
        lengths = []

        #convert input to ascii values, with commas in between
        for x in range(0,len(inputlengths) ):
                for char in str(inputlengths[x]):
                        lengths.append( ord(str(char))  )

        salt = [17, 31, 73, 47, 23]

        #add salt
        for value in salt:
                lengths.append( value )



        current = 0
        skip = 0

        buffer = []

        #Allows looping round to start of arrays when index is too high
        def getElement( index ):
                while index >= len(elements):
                        index -= len(elements)
                return elements[index]

        def getIndex( index ):
                while index >= len(elements):
                        index -= len(elements)
                return index

        for x in range( 0,64):
                for value in lengths:
                        buffer = []
                        for x in range( 0, value ):
                                buffer.append( getElement( x+current ) )

                        for x in range( 0,value ):
                                elements[ getIndex( x+current ) ] = buffer.pop()
                        
                        current = getIndex( current + value + skip )
                        skip += 1
                        
        #xor blocks of output together
        position = 0
        current = 0
        postxor = []
        while position < len(elements):
                current = elements[position]
                for x in range(1,16):
                        current = current ^ elements[position+x]
                postxor.append( current )
                position += 16
                
        #add preceeding zero if missing
        def preZero(input):
                if( len(input) == 1 ):
                        return str(0)+str(input)
                return str(input)

        #convert to hex string:
        hexstring = ''
        for value in postxor:
                hexstring = hexstring + preZero(hex(value)[2:])

        return hexstring

#convert hex to four binary didgets
def convertBin( input ):
        answer = str( bin(int(input, 16))[2:] )
        padding = 4 - len(answer)
        for x in range ( 0, padding ):
                answer = '0' + answer
        return answer
        

#input is fixed for this one:
#input = 'flqrgnkx'
input = 'xlqgujun'

gridSize = 128
hashGrid = []
#result = 0
groups = 0

for x in range(0,gridSize):
        currentInput = input+'-'+str(x)
        resultHash = knotHash( currentInput )
        thisline = ''
        for char in resultHash:
                byte = ( convertBin( char ) )
                thisline += byte
        
        hashGrid.append( thisline )

print( str( hashGrid[3] ) )
        
def findNextOne():
        for x in range( 0,len(hashGrid ) ):
                currentWord = hashGrid[x]
                for y in range( 0,len( currentWord ) ):
                        if currentWord[y] == '1':
                                result = []
                                result.append(x)
                                result.append(y)
                                return result
        
        return -1

def checkExistingOrZero( firstGroup, secondGroup, target ):
        for item in firstGroup:
                if item[0] == target[0] and item[1] == target[1]:
                        return True

        for item in secondGroup:
                if item[0] == target[0] and item[1] == target[1]:
                        return True
        
        if hashGrid[ target[0] ] [target[1] ] == '0':
                return True
        return False

def exploreAndClearGroup( input ):
        #input should be y and x value for startpoint so..
        members = []
        unexplored = []
        unexplored.append(input)
        #add neighbours of input to unexplored (if they aren't already in either list)
        while( len(unexplored) > 0 ):
                currentMember = unexplored.pop()
                members.append( currentMember )
                #print("adding " + str(currentMember) )
                #check above
                
                if currentMember[0] > 0:
                        candidate = [currentMember[0]-1,currentMember[1]  ]
                        if checkExistingOrZero( members, unexplored,candidate  ) == False:
                                unexplored.append( candidate )
                        
                
                #check left
                if currentMember[1] > 0:
                        candidate = [currentMember[0], currentMember[1]-1 ]
                        if checkExistingOrZero( members,unexplored,candidate ) == False:
                                unexplored.append( candidate )

                #check right
                if currentMember[1] < ( len( hashGrid[ currentMember[0] ] ) - 1 ):
                        candidate = [currentMember[0], currentMember[1]+1 ]
                        if checkExistingOrZero( members, unexplored, candidate ) == False:
                                unexplored.append( candidate )

                #check below
                if currentMember[0] < ( len(hashGrid) -1 ):
                        candidate = [currentMember[0]+1,currentMember[1] ]
                        if checkExistingOrZero( members, unexplored, candidate ) == False:
                                unexplored.append( candidate )
        
        #now remove all members of the group from the grid
        for member in members:
                currentWord = hashGrid[ member[0] ]
                
                targetPoint = member[1]
                currentWord = currentWord[:targetPoint] + '0' + currentWord[ targetPoint+1:]
                hashGrid [ member[0] ] = currentWord

#hash grid for testing
                
#test grid should have 4 groups
#hashGrid = [ '1001','1100','0000','0101']
#print( str(hashGrid) )
currentGroup = []

searchEnded = False
while searchEnded == False:
        nextOne = findNextOne()
        if nextOne == -1:
                searchEnded = True
        else:
                groups += 1
                #use next one to establish group
                exploreAndClearGroup( nextOne )
                #print( str(hashGrid) )

print('finished')
print (str( groups ) )
#print ( str(hashGrid) )
#print( hashGrid[0] )
#print( str(result) )


#do this for all 128

#count 1s and print result

#***************












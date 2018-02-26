#Advent of Code '17
#Day 10a: Knot hash

#elements = [0,1,2,3,4]
elements = []
for x in range( 0,256):
        elements.append( x )

#lengths = [3,4,1,5]
lengths = [76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229]

current = 0
skip = 0

buffer = []

#Allows looping round to start of arrays when index is too high
def getElement( index ):
        if index >= len(elements):
                index -= len(elements)
        return elements[index]

def getIndex( index ):
        if index >= len(elements):
                index -= len(elements)
        return index

for value in lengths:
        #print( str(value) )
        buffer = []
        for x in range( 0, value ):
                buffer.append( getElement( x+current ) )

        for x in range( 0,value ):
                elements[ getIndex( x+current ) ] = buffer.pop()

        
        current = getIndex( current + value + skip )
        skip += 1
        print( str(elements) + "  " + str(current) + "  " + str(skip) )


print('done')
print('Output: ' + str( elements[0] * elements[1] ) )



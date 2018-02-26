#Advent of Code '17
#Day 10b: Knot hash

#elements = [0,1,2,3,4]
elements = []
for x in range( 0,256):
        elements.append( x )



#inputlengths = [1,2,3]
inputlengths = [76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229]
lengths = []

#convert input to ascii values, with commas in between
for x in range(0,len(inputlengths) ):
        for char in str(inputlengths[x]):
                lengths.append( ord(str(char))  )
        if x!= len(inputlengths)-1:
                lengths.append(44)

salt = [17, 31, 73, 47, 23]

#add salt
for value in salt:
        lengths.append( value )

print("After the conversion:")


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

print ('lengths ' + str(lengths) )

for x in range( 0,64):
        for value in lengths:
                #print( str(value) )
                buffer = []
                #print(value)
                for x in range( 0, value ):
                        buffer.append( getElement( x+current ) )

                for x in range( 0,value ):
                        elements[ getIndex( x+current ) ] = buffer.pop()

                
                current = getIndex( current + value + skip )
                skip += 1
                #print( str(elements) + "  " + str(current) + "  " + str(skip) )

print("after mixing: " + str(elements) )
print( len(elements) )

#Xor test
#xortest = [65, 27, 9, 1 , 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]


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
        
print( str(len( postxor )) )
print( str(postxor) )

#add preceeding zero if missing
def preZero(input):
        if( len(input) == 1 ):
                return str(0)+str(input)
        return str(input)

#convert to hex string:
hexstring = ''
for value in postxor:
        hexstring = hexstring + preZero(hex(value)[2:])

print(hexstring)

print('done')
print('Output: ' + str( elements[0] * elements[1] ) )



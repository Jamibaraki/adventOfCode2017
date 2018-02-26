#Advent of Code '17
#Day 10b: Knot hash

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
                #lengths.append( ord(str(inputlengths[x]))  )
                if x!= len(inputlengths)-1:
                        lengths.append(44)

        salt = [17, 31, 73, 47, 23]

        #add salt
        for value in salt:
                lengths.append( value )

        #print("After the conversion:")

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
                        #print( str(value) )
                        buffer = []
                        #print(value)
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

        #print(hexstring)
        return hexstring

#print( knotHash( [76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229] ) )
print( knotHash ( 'flqrgnkx-0' ) )

#Advent of Code '17
#Day 14a - Disk Defragmentation


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

result = 0

for x in range(0,gridSize):
        currentInput = input+'-'+str(x)
        #print( currentInput )
        resultHash = knotHash( currentInput )
        for char in resultHash:
                byte = ( convertBin( char ) )
                for bit in byte:
                        if bit == '1':
                                result += 1
                

print('finished')
print( str(result) )
#print( convertBin( '1' ) )

#do this for all 128

#count 1s and print result

#***************












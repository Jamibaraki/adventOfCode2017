#Advent of Code '17
#Day 15b - Duelling Generators part 2

def generate( input, factor ):
        result = ( input * factor ) % 2147483647
        return result

def generatorA( input ):
        passed = False
        while passed == False:
                answer = generate( input, 16807 )
                if answer % 4 == 0:
                        return answer
                input = answer
        return -1
        #return generate( input, 16807 )

def generatorB( input ):
        passed = False
        while passed == False:
                answer = generate( input, 48271 )
                if answer % 8 == 0:
                        return answer
                input = answer
        return -1
        #return generate( input, 48271 )

#print( str( generatorA( 65 ) ) )

#print( str( generatorB( 8921 ) ) )


currentA = 116 #65
currentB = 299 #8921
bitsA = 0
bitsB = 0

def judge():
        global currentA
        global currentB
        currentA = generatorA( currentA )
        currentB = generatorB( currentB )

pairs = 0
maxPairs = 5000000 #1100 #5 #40000000

hits = 0

while pairs < maxPairs:
        judge()
        bitsA = bin(currentA)
        bitsB = bin(currentB)
        #check if last 16 chars match..
        if len( bitsA ) > 16 and len( bitsB ) > 16:
                hit = True
                for x in range( 0,16 ):
                        if bitsA[ len(bitsA)-1-x ] != bitsB[ len(bitsB)-1-x ]:
                                hit = False
                if hit == True:
                        hits += 1

        pairs += 1        
        
print( str( hits ) )




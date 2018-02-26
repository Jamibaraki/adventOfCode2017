#Recursive Circus
#Advent of Code 2017
#Day 7b
print("reading file")
#file = open('inputTest.txt','r')
file = open('input7.txt','r')
input = file.read()
file.close()

lines = input.split("\n")



#find the index of a word
def getWordIndex( target ):
    for x in range( 0, len(lines) ):
        parts = lines[x].split(" ")
        if( target == parts[0] ):
            return x
    #if we don't find it.. hmm
    print("getWordIndex failed in its quest "+target)
    return -1

#Calculate the weights of those above
def calcTowers():
    #for each tower
    for x in range( 0, len(lines) ):
        if getWeight(x) == False:
            return
    print("Didn't find a naughty one")
        
def printIndexName(index):
    parts = lines[index].split(" ")
    print( parts[0] )
              
def getWeight(index):
    parts = lines[index].split(" ")
    #add the weights of those above
    weight = 0
    weight += int(parts[1].strip("()"))
    #print( str( weight ) )
    bail = False
    if len(parts) > 2:
        partWeights = []
        for y in range( 3 , len(parts)  ):
            word = parts[y].strip(",")
            partWeights.append( getWeight( getWordIndex( word ) ) )
            if( len(partWeights) > 1 and partWeights[0] != partWeights[len(partWeights)-1] ):
                print( "The naughty index is number " + str(index) )
                print( partWeights )
                printIndexName( index )
                bail = True
        for eachWeight in partWeights:
            weight += eachWeight
        if( bail ):
            print( "The Offending weights: " )
            for eachWeight in partWeights:
                print( eachWeight )
            return False
    #print( parts[0] + str( weight) )
    return weight


#print( printIndexName( 880 ) )
#print( getWeight(880) )
calcTowers()

#requires a bit of further deduction from result..
                
    

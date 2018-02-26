file = open('input.txt','r')
input = file.read()

#test input
#input = "12131415"
#print( input )
file.close()

sum = 0
inputLength = len(input)
split = int( inputLength/2 )


#sum of numbers that match digits
for x in range(0,inputLength):
    comparisonIndex = x + split
    if comparisonIndex > ( inputLength-1 ):
        comparisonIndex -= inputLength
        #print( comparisonIndex )

    if input[x] == input[comparisonIndex]:
        sum += int( input[x])

#do last one as edge case..
#if( inputLength > 1 ):
#    if( input[inputLength-1] == input[0] ):
#        sum += int(input[0])

print ("finished" )
print ( sum )

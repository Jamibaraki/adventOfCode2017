file = open('input.txt','r')
input = file.read()

#test input
#input = "91212129"
#print( input )
file.close()

sum = 0
inputLength = len(input)

#sum of numbers that match digits
for x in range(0,inputLength-1):
    if input[x] == input [x+1]:
        sum += int( input[x])

#do last one as edge case..
if( inputLength > 1 ):
    if( input[inputLength-1] == input[0] ):
        sum += int(input[0])

print ("finished" )
print ( sum )

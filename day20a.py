#Advent of Code 20a
# A Particle Swarm


import re

print('Particle Swarm')
#file = open('inputTest.txt','r')
file = open('input20.txt','r')
input = file.read().split('\n')
file.close()

#hypothesis - we just need to figure out the lowest acceleration..
#in the long term that will always be closer
#there may be a tie for this..
lowestTotal = 100000000
closest = []

#parse the particles
#for particle in input:
for x in range( 0, len(input) ):    
    group = re.findall('\<.*?\>',input[x])
    print( str( len( group ) ) )
    print( group[2] )
    nums = group[2].split(',')
    total = 0
    for num in nums:
        num = int( num.strip("<>") )
        print( str(num) )
        total += abs(num)
    if total < lowestTotal:
        lowestTotal = total
        closest = []
        closest.append(x)
    elif total == lowestTotal:
        closest.append(x)
    #for item in group:
    #    print( group )
print( "Lowest: " + str( lowestTotal ) )
print( closest )


#copy the closest to candidates list
candidates = []
for item in closest:
    candidates.append( input[item] )
    print( input[item] )
#print( input[119] )
#print( input[299] )
#print( input[516] )
print( str(len(candidates)))


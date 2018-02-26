#Advent of Code 17b

import time

#state = [0,1,2,3,4]
state = [0]
position = 0
#jumps = 3
jumps = 370

stateLength = 1
zeroPosition = 0
answer = 0

#the next value to insert
value = 1
start_time = time.time()
#should take about 10 minutes..
#actually taking forever because increasing exponentially
#1mill=1m40 2mill = 9m16 3mill = > 21mins
#two possible solutions:
#1. linked list
#2. Dont have a list, just have an int for its size
#keep track of position 1, and record anything added after it.

counter = 0
millions = 0

for x in range( 0,50000000 ):
#for x in range( 0,5 ):
        #move pointer <jumps number of times>
        position += jumps
        if position >= stateLength:
                position = position % stateLength

        if position == 0:
                answer = value

                
        stateLength += 1
        
        position += 1
        value += 1

        counter += 1
        if counter == 1000000:
                millions+= 1
                counter = 0
                print("mills: " + str(millions) )
        
print(time.time() - start_time )

print( str( zeroPosition ) )
print( str( answer ) )

#print(position)
print(state)
#print(state[position])
#print(state[position+1])
#print(state[position+2])



#Memory Reallocation
#Advent of Code 2017 Day 6

import numpy as np


input = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"
banks = input.split("\t")
banks = [ int(x) for x in banks ]
banks = [0, 2, 7, 0]
steps = 0

previous = []

matched = False


while matched == False:
    #store current config in history

    previous.append( np.copy( banks ) )
    
    #Find the biggest bank
    biggest = 0
    for x in range( 0, len(banks) ):
        if( banks[x] > banks[biggest] ):
            biggest = x

    #Take blocks out of biggest
    toGive = banks[biggest]
    banks[biggest]=0
    current = biggest
    
    #redistribute
    while toGive > 0 :
        current += 1
        if( current >= len( banks ) ):
            current = 0

        banks[current] += 1
        
        toGive -=1

    steps += 1
    
    #check for previous matches
    for bank in previous:
        if np.array_equal( bank, banks ):
            print( str(bank) + "..." + str(banks) ) 
            matched = True
        




print("Finished: " + str(steps) )



    



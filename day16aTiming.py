#Advent of Code '17
#Day 16a Permutation Promenade

def getIndex( value ):
        for x in range(0,len(programs) ):
                if programs[x] == value:
                        return x
        print("get Index found nothing")
        return -1

def spin( size ):
        global programs
        size = len(programs) - size
        programs = programs[size:] + programs[:size]



def partner( first, second ):
        global programs
        indexOne = getIndex( first )
        indexTwo = getIndex( second )
        programs[indexOne],programs[indexTwo] = programs[indexTwo],programs[indexOne]

#programs = ['a','b','c','d','e']
programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

#spin(1)
#exchange( 4, 3 )
#partner( 'e','b')

#read input
#file = open('inputTest.txt','r')
file = open('input16.txt','r')
input = file.read().split(',')
file.close()

def dance():
        for instruction in input:        
                #print( instruction )
                if instruction[0] == 's':
                        #spin
                        value = int ( instruction[1:] ) #1 sec
                        spin( value ) #2sec
                elif instruction[0] == 'x':
                        #exchange
                        values = instruction[1:].split('/')
                        
                        first = int( values[0] )
                        second = int( values[1] )
                        programs[first],programs[second] = programs[first],programs[second]
                elif instruction[0] == 'p':
                        #partner
                        partner( instruction[1], instruction[3] )

import time
#timing this to figure out how long to do a billion times..
#1000 times take 12.5 seconds. Hmm. 139 days with current code to do it all..
#sticking the loop in a function: 11.12
#removed exchange function: 10.6
#Abandoning this - the correct approach is to map the final positions after the dance runs once
#and apply the same same positional transformations repeatedly without doing the whole shebang!
start_time = time.time()
#parse the instructions
for x in range( 0, 1000 ):
        dance()


        
print(time.time() - start_time )
print( str(programs) )

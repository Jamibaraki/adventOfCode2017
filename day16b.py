#Advent of Code '17
#Day 16b Permutation Promenade

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

def exchange( first, second ):
        global programs
        temp = programs[first]
        programs[first] = programs[second]
        programs[second] = temp

def partner( first, second ):
        global programs
        indexOne = getIndex( first )
        indexTwo = getIndex( second )
        exchange( indexOne, indexTwo )


#programs = ['a','b','c','d','e']
startState = programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
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
        #parse the instructions
        for instruction in input:
                #print( instruction )
                if instruction[0] == 's':
                        #spin
                        value = int ( instruction[1:] )
                        #print( str( value ) )
                        spin( value )
                elif instruction[0] == 'x':
                        #exchange
                        #print('x')
                        values = instruction[1:].split('/')
                        exchange( int( values[0] ), int( values[1] ) )
                        #print( values )
                elif instruction[0] == 'p':
                        #partner
                        #print('p')
                        partner( instruction[1], instruction[3] )

def cookedDance():
	global programs
	#seperate the cooked dance into one set of swaps for the positions (spin and exchange operation)
	programs = [ programs[14], programs[3],programs[15],programs[10],programs[12],programs[9],programs[13],programs[7],programs[2],programs[1],programs[6],programs[8],programs[0],programs[11],programs[4],programs[5] ]
	# and one set of swaps for the letters (partner operation)
	#programs = [ programs[], programs[],programs[],programs[],programs[],programs[],programs[],programs[],programs[],programs[],programs[],programs[],programs[],programs[],programs[],programs[] ]
	partner( 'a','n' )
	partner( 'k','o' )
	partner( 'b','l' )
	partner( 'h','c' )
	partner( 'd','p' )
	partner( 'e','m' )
	partner( 'g','i' )
	partner( 'c','j' )
	partner( 'c','g' )
	partner( 'e','g' )
	partner( 'b','g' )
	partner( 'b','d' )
	#combined position one doesn't work..
	#programs = [ programs[10], programs[15],programs[1],programs[14],programs[3],programs[4],programs[0],programs[9],programs[7],programs[11],programs[8],programs[2],programs[13],programs[6],programs[12],programs[5] ]

#import time
#start_time = time.time()
#for x in range( 0, 1000000000 ):

#following loop shows the state repeats every 43 times..
##for x in range( 0, 1000000 ):
##        dance()
##        if programs == startState:
##                print( str(x+1) + ' iterations' )
##                break

#repeats after 44 dances
#print ( 1000000000 % 44 )
#so loop 32 times..

for x in range( 0, 32 ):
        dance()


#print(time.time() - start_time )
#print( str(programs) )
result = ""
for letter in programs:
        result += letter
print( result )
# keafhbmgplionjcd

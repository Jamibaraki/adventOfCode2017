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
programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

#spin(1)
#exchange( 4, 3 )
#partner( 'e','b')

#read input
#file = open('inputTest.txt','r')
file = open('input16.txt','r')
input = file.read().split(',')
file.close()

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

print( str(programs) )

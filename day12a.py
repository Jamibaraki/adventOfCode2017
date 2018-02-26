#Advent of Code '17
#Day 12a: Digital Plumber


import re


#read input
file = open('input12.txt','r')
input = file.read().split('\n')
file.close()

#list of which we have found to be connected
connected = []

toAdd = [0]

for x in range(0, len(input)):
        input[x] = input[x].split(' ')
        connected.append( False )
        


totalConnections = 0

while( len(toAdd) ):
        nextLine = toAdd.pop()
        #print(nextLine)
        if connected[nextLine] == False:
                connected[nextLine] = True
                totalConnections += 1
                for value in range( 2, len(input[nextLine]) ):
                        number = re.sub("[^0-9]","",input[nextLine][value])
                        toAdd.append( int(number) )



                       
print( "Connections: " + str(totalConnections) )



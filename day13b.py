#Advent of Code '17
#Day 13a: Packet Scanners

#This runs slowly with proper data!
#Quicker to optimise than run again
#Check 13b2.py for optimized version

import platform
print ( platform.python_implementation() )

import re

#read input
file = open('input13.txt','r')
input = file.read().split('\n')
file.close()

#get list of scanners from input
#each scanner is array with four values - position, size, current position and direction
#direction = 1 for moving down. -1 for moving up
scanners = []

furthestScanner = 0

for line in input:
        line = line.split(' ')
        #print( str( line[1] ) )
        line[0] = re.sub("[^0-9]","",line[0])
        scanners.append( [ int(line[0]) ,int( line[1] ),0, 1 ] )

        #keep track of the furthest scanner
        if int(line[0]) > furthestScanner:
                furthestScanner = int(line[0])
        #print( str(scanners) )

#print("furthest scanner " + str(furthestScanner) )

def incPositions():
        for scanner in scanners:
                if scanner[3] == 1:
                        scanner[2] += 1
                        if scanner[2] >= scanner[1]:
                                scanner[2] -= 2
                                scanner[3] = -1
                elif scanner[3] == -1:
                        scanner[2] -= 1
                        if scanner[2] < 0:
                                scanner[2] = 1
                                scanner[3] = 1


#for x in range( 0,5 ):
#        #print( str(scanners) )
#        incPositions()
      
#move through and detect where we are caught
#should be 0 and 6 for test

#determing largest



#def checkSeverity( delay, display ):
def checkCaught( delay ):
        severity = 0

        #resetPositions
        for scanner in scanners:
                scanner[2] = 0
                scanner[3] = 1
        
        #do delay
        if delay > 0:
                while delay > 0:
                        incPositions()
                        delay -= 1
        
        #x represents position of moving user in main loup
        for x in range( 0, furthestScanner+1 ):
                        for y in range( 0, len(scanners) ):
                                if scanners[y][0] == x:
                                        #print("hit " + str(x) + " " + str( scanners[y][2] ) )
                                        if scanners[y][2] == 0:
                                                #print("scanner caught us. Position: " + str(x) )
                                                return True
                        #if display:
                        #        print( str(scanners) + " " + str(x) )
                        incPositions()
        #print( "severity: " + str(severity) )
        return False

# result > following so may as well start from here
attempt = 53000
counter = 0
#result = checkSeverity( attempt, False )
result = checkCaught( attempt )
if result == True:
        while result != False and attempt < 125000:     
                if counter == 1000:
                        print ( "thousand ticks" + str( attempt ) )
                        counter = 0
                counter += 1
                attempt += 1
                #result = checkSeverity( attempt, False )
                result = checkCaught( attempt )
                

print( str( attempt ) )
#checkSeverity( attempt, True )

#print( "Severity: " + str(severity) )
                                
                








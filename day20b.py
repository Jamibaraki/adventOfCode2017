#Advent of Code 20b
# A Particle Swarm



def addVector( vec1, vec2 ):
    vec1[0] += vec2[0]
    vec1[1] += vec2[1]
    vec1[2] += vec2[2]
    return vec1

def moveParticle( particle  ):
    particle[1] = addVector( particle[1], particle[2] )
    particle[0] = addVector( particle[0], particle[1] )
    return particle

def printItems():
    for item in input:
        print( item )

import re
import time

print('Particle Swarm')
#file = open('inputTest.txt','r')
file = open('input20.txt','r')
input = file.read().split('\n')
file.close()

#hypothesis - we just need to figure out the lowest acceleration..
#in the long term that will always be closer
#there may be a tie for this..

start_time = time.time()

#parse the particles
#for particle in input:
for x in range( 0, len(input) ):    
    group = re.findall('\<.*?\>',input[x])
    newentry = []
    #print( str( len( group ) ) )
    #print( group[2] )

    for item in group:
    
        #nums = group[2].split(',')
        nums = item.split(',')
        newnums = []
        for num in nums:
            num = int( num.strip("<>") )
            newnums.append(num)
        newentry.append( newnums )
    input[x] = newentry

print(time.time() - start_time )




#printItems()
#numbers are now processed into three arrays representing x,y,z for
#position, velicity and acceleration
running = True
count = 0
limit = 500

particleCount = len(input)

while running:
    count += 1
    if count == limit:
        running = False
    for particle in input:
        particle = moveParticle( particle )

    hitlist = []
    
    #check all particles for collision, form list of colliding particles
    
    for x in range( 0, particleCount ):
        for y in range( x+1, particleCount ):
            if( input[x][0] == input[y][0] ):
                hitlist.append( x )
                hitlist.append( y )
    if len( hitlist ):
        hitlist = list(set(hitlist) )
        print( hitlist )
        for index in sorted( hitlist, reverse=True ):
            del input[index]
        particleCount = len(input)
        print( str(particleCount) )
        print(time.time() - start_time ) 
    #for each member of hitlist

print("finished!")
print(time.time() - start_time ) 

#printItems()    

    
        
    
    





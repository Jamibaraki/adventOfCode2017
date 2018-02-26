#Advent of Code '17
#Day 11b: Hex Ed

import math

#x,y
position = [0,0]

#input = ['ne','ne','ne']
#input = ['ne','ne','sw','sw']
#input = ['ne','ne','s','s']
#input = ['se','sw','se','sw','sw']

#read input
file = open('input11.txt','r')
input = file.read().split(',')
file.close()

highestmoves = 0

for value in input:
        
        if value == 'ne':
                position[0] = position[0] + 1
                position[1] = position[1] - 0.5
        elif value == 'n':
                position[1] = position[1] - 1
        elif value == 'se':
                position[0] = position[0] + 1
                position[1] = position[1] + 0.5
        elif value == 's':
                position[1] = position[1] + 1
        elif value == 'sw':
                position[0] = position[0] - 1
                position[1] = position[1] + 0.5
        elif value == 'nw':
                position[0] = position[0] - 1
                position[1] = position[1] - 0.5

        xdistance = math.fabs( position[0] )
        ydistance = math.fabs( position[1] )

        moves = 0

        while xdistance > 0 or ydistance > 0:
                if xdistance == 0:
                        ydistance -= 1
                else:
                        xdistance -= 1
                        if ydistance > 0:
                                ydistance -= 0.5
                moves += 1

        if moves > highestmoves:
                highestmoves = moves

print("highestmoves: " + str(highestmoves ) )
                

print('after moving: ' + str(position) )

#Advent of Code 25a
#The Halting Problem
print('electromagnetic moat')


import time
start_time = time.time()


state = 'A'
values = []
negativeValues = []

cursor = 0

#if cursor moves to negative position read from negative values. Cursor -1 = negativeValues 0,   cursor -2 = negativeValues 1

opCount = 0
opLimit = 12459852 #6

def getCurrentValue():
    if cursor >= 0:
        if cursor >= len(values):
            return 0
        else:
            return values[cursor]
    elif cursor < 0:
        tocheck = abs(cursor) - 1
        if tocheck >= len(negativeValues):
            return 0
        else:
            return negativeValues[tocheck]

    print('getCurrentValue error')
    return 0

def setCurrentValue(value):
    if cursor >= 0:
        if cursor >= len(values):
            values.append( value )
        else:
            values[cursor] = value
        return
    elif cursor < 0:
        tocheck = abs(cursor) - 1
        if tocheck >= len(negativeValues):
            negativeValues.append(value)
        else:
            negativeValues[tocheck] = value
        return

    print('setCurrentValue error')

    

while opCount < opLimit:
    opCount+= 1
    
    if state == 'A':
        if getCurrentValue() == 0:
            setCurrentValue(1)
            cursor += 1
            state = 'B'
        elif getCurrentValue() == 1:
            setCurrentValue(1)
            cursor -= 1
            state = 'E'
        
    elif state =='B':
        if getCurrentValue() == 0:
            setCurrentValue(1)
            cursor += 1
            state = 'C'
        elif getCurrentValue() == 1:
            setCurrentValue(1)
            cursor += 1
            state = 'F'

    elif state =='C':
        if getCurrentValue() == 0:
            setCurrentValue(1)
            cursor -= 1
            state = 'D'
        elif getCurrentValue() == 1:
            setCurrentValue(0)
            cursor += 1
            state = 'B'

    elif state =='D':
        if getCurrentValue() == 0:
            setCurrentValue(1)
            cursor += 1
            state = 'E'
        elif getCurrentValue() == 1:
            setCurrentValue(0)
            cursor -= 1
            state = 'C'

    elif state =='E':
        if getCurrentValue() == 0:
            setCurrentValue(1)
            cursor -= 1
            state = 'A'
        elif getCurrentValue() == 1:
            setCurrentValue(0)
            cursor += 1
            state = 'D'

    elif state =='F':
        if getCurrentValue() == 0:
            setCurrentValue(1)
            cursor += 1
            state = 'A'
        elif getCurrentValue() == 1:
            setCurrentValue(1)
            cursor += 1
            state = 'C'
            
##    if state == 'A':
##        if getCurrentValue() == 0:
##            setCurrentValue(1)
##            cursor += 1
##            state = 'B'
##        elif getCurrentValue() -- 1:
##            setCurrentValue(0)
##            cursor -= 1
##            state = 'B'
##        
##    elif state =='B':
##        if getCurrentValue() == 0:
##            setCurrentValue(1)
##            cursor -= 1
##            state = 'A'
##        elif getCurrentValue() == 1:
##            setCurrentValue(1)
##            cursor += 1
##            state = 'A'

result = 0
#count the ones and display them
for value in values:
    if value == 1:
        result += 1

for value in negativeValues:
    if value == 1:
        result += 1

print( result )
#print( values )
#print( negativeValues )

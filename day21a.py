#Advent of Code 21a
# Fractal Art

import numpy as np

#counts active pixels (ie '#')
def countPixels(input):
    count = 0
    for item in input:
        count += item.count('#')
    return count

def verticalFlip(input):
    output = []
    for item in reversed( input ):
        output.append( item )
    return output

def horizontalFlip(input):
    output = []
    for item in input:
        output.append( item[::-1] )
    return output

def rotate(input):
    output = []
    size = len(input)
    for x in range(0,size):
        output.append( input[size-1][x] )

    for y in range(1,size):
        for x in range(0,size):
            output[x] = output[x] + ( input[size-1-y][x] )
    return output

#generate array containing origianl, rotated and flipped versions of rule
def getRuleVariations( rule ):
    rule_set = []
    rule_set.append( rule ) #append the original rule

    #vertical flip
    new_rule = []
    new_source = verticalFlip( rule[0] )
    new_rule.append( new_source )
    new_rule.append( rule[1] )
    rule_set.append( new_rule )

    #horizontal flip
    new_rule = []
    new_source = horizontalFlip( rule[0] )
    new_rule.append( new_source )
    new_rule.append( rule[1] )
    rule_set.append( new_rule )

    #rotation 180
    new_rule = []
    half_turn_source = verticalFlip( horizontalFlip( rule[0] ) )
    new_rule.append( half_turn_source )
    new_rule.append( rule[1] )
    rule_set.append( new_rule )
    
    #rotation 90 functinon..
    new_rule = []
    new_source = rotate( rule[0] )
    new_rule.append( new_source )
    new_rule.append( rule[1] )
    rule_set.append( new_rule )
    
    #apply it to 180..
    new_rule = []
    next_source = rotate( half_turn_source )
    new_rule.append( next_source )
    new_rule.append( rule[1] )
    rule_set.append( new_rule )

    #flip the last one
    new_rule = []
    new_source = horizontalFlip( next_source )
    new_rule.append( new_source )
    new_rule.append( rule[1] )
    rule_set.append( new_rule )
                     

    #rotation vflip plus rotate 90
    new_rule = []
    new_source = verticalFlip( rule[0] )
    new_source = rotate( new_source )
    new_rule.append( new_source )
    new_rule.append( rule[1] )
    rule_set.append( new_rule )
    
    return rule_set

import time
start_time = time.time()
print('Fractal Art')
#file = open('inputTest.txt','r')
file = open('input21.txt','r')
input = file.read().split('\n')
file.close()

#parse input
#sort rules and put them into arrays
two_by_two_rules = []
three_by_three_rules = []
for x in range( 0, len(input) ):
    line = input[x].split(' ')
    #print( str(len(line) ) )

    #rule 0 will be the start state and rule 1 will be the end state
    rule = []
    rule.append( line[0].split('/') )
    rule.append( line[2].split('/') )
    if len(rule[0][0]) == 2:
        # get a set of flipped and rotated rules
        rules = getRuleVariations( rule )
        #then replace this with adding all the rules in the array
        for rule in rules:
            two_by_two_rules.append( rule )
        #two_by_two_rules.append( rule )
        
    elif len(rule[0][0]) == 3:
        rules = getRuleVariations( rule )
        for rule in rules:
            three_by_three_rules.append( rule )
        #three_by_three_rules.append( rule )
    else:
        print("wrong sized rule, taihen")

#print( two_by_two_rules )

for rule in three_by_three_rules:
    pass
    #print( rule )
#print( three_by_three_rules )

for rule in two_by_two_rules:
    #print( rule )
    pass

print(str( len(input) ))
print(str(len(two_by_two_rules)))
print(str(len(three_by_three_rules)))
print('**')
    

pattern = []
pattern.append('.#.')
pattern.append('..#')
pattern.append('###')

#print(pattern)

#run it for five iterations
#get it tiling multiple new sections
#get it searching for flipped and rotated versions

#while done = False

def replacePattern( oldPattern, ruleset ):

    if ruleset == 2:
        #two by two version
        for rule in two_by_two_rules:
            if rule[0] == oldPattern:
                #print("found it")
                return rule[1]

    if ruleset == 3:
        #three by three version
        for rule in three_by_three_rules:
            if rule[0] == oldPattern:
                #print("found it, 3")
                return rule[1]
    
    print("replacePattern didn't find a rule "+str(ruleset))
    print( oldPattern )

#print( three_by_three_rules )

#do for five iterations
iterations = 5
for iteration in range(0,iterations):

    size = len(pattern)
    #if size is divisible by 2 - split into two by two squares and enhance into 3x3
    if size % 2 == 0:
        print("div by 2")
        squares = int( size/2 )
        new_pattern = []
        
        for yAxis in range(0,squares):
            for xAxis in range(0,squares):
                #add new chunks to new pattern, then push them all to a new two lines of the new pattern
                #determine existing pattern
                patternToCheck = []
                patternToCheck.append( pattern[yAxis*2][xAxis*2:xAxis*2+2] )
                patternToCheck.append( pattern[yAxis*2+1][xAxis*2:xAxis*2+2] )
                #print( patternToCheck )
                newChunk = replacePattern( patternToCheck, 2 )
                #print("newchunk: ")
                #print( newChunk )
                #for row in newChunk:
                #print(xAxis,yAxis )
                newSize = 3
                for row in range(0,len(newChunk)):
                    if xAxis == 0:
                        new_pattern.append(newChunk[row])
                    else:
                        new_pattern[yAxis*newSize+row] += (newChunk[row])
                #print("New pattern: " + str( new_pattern))
                
                
                
                
        #check for a matching pattern in the two rules

        #check for flipped and rotated versions
        # do the flipping and rotating at the rule parsing stage

    #if size is divisible by 3 - break into 3x3 squares and enhance into 4x4
    elif size % 3 == 0:
        print("div by 3")
        squares = int(size/3)
        new_pattern = []
        print(squares)
        for yAxis in range(0,squares):
            for xAxis in range(0,squares):
                patternToCheck = []
                patternToCheck.append( pattern[yAxis*3][xAxis*3:xAxis*3+3] )
                patternToCheck.append( pattern[yAxis*3+1][xAxis*3:xAxis*3+3] )
                patternToCheck.append( pattern[yAxis*3+2][xAxis*3:xAxis*3+3] )
                #
                newChunk = replacePattern( patternToCheck, 3 )
                #
                newSize = 4
                for row in range(0,len(newChunk)):
                    if xAxis == 0:
                        new_pattern.append(newChunk[row])
                    else:
                        new_pattern[yAxis*newSize+row] += (newChunk[row])

        
    else:
        print("grid size error")

    pattern = new_pattern

print("Pixel count: " + str( countPixels( pattern ) ) )

print(time.time() - start_time )

#print( pattern )

#for line in pattern:
#    print( line )


      
    
    





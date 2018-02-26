#Jumping through array
#Advent of Code 2017 Day 5


#instructions = [0,3,0,1,-3]

file = open('input5.txt','r')
input = file.read()
file.close()
#print (input)

instructions = [int(n) for n in input.split() ]
print( len(instructions) )

index = 0
jumps = 0
escaped = False



while escaped == False:

    toJump = instructions[index]
    instructions[index] += 1
    index += toJump
    jumps += 1

    if( ( index < 0 ) or (index >= len(instructions) ) ):
        escaped = True
        break


print( "Escaped! Jumps: " + str(jumps) )
    



#I heard you like registers
#Advent of Code 2017
#Day 8
print("reading file")
#file = open('inputTest.txt','r')
file = open('input8.txt','r')
input = file.read()
file.close()

lines = input.split("\n")



largest = 0

#registers = { "a":3, "b":4 }
registers = {}
def checkRegister( index ):
    if index in registers:
        return registers[index]
    return 0

#print( checkRegister( "c" ) )
#print( checkRegister( "b" ) )

def checkCondition( input ):
    
    termA = checkRegister( input[4] )
    termB = int( input[6] )
    operator = input[5]
    
    if operator == ">":
        return termA > termB
    if operator == "<":
        return termA < termB
    if operator == ">=":
        return termA >= termB
    if operator == "<=":
        return termA <= termB
    if operator == "==":
        return termA == termB
    if operator == "!=":
        return termA != termB
    return False

for line in lines:
    line = line.split(" ")
    #print( checkCondition( line ) )
    if checkCondition( line ):
        #now inc or dec
        if line[1] == "inc":
            registers[ line[0] ] = checkRegister( line[0] ) + int(line[2])
        if line[1] == "dec":
            registers[ line[0] ] = checkRegister( line[0] ) - int(line[2])

#print( registers )
for value in registers:
    #print( registers[value] )
    if registers[value] > largest:
        largest = registers[value]

print( largest )


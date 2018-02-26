#Advent of Code 18a
# Duet


file = open('input18.txt','r')
#file = open('inputTest.txt','r')
input = file.read().split('\n')
file.close()



registerLetters = 'abcdefghijklmnop'
registerLetterLength = len( registerLetters )
registerValues = []
for letter in registerLetters:
        registerValues.append( 0 )

def getRegisterPosition(input):
        for x in range(0, registerLetterLength):
                if input == registerLetters[x]:
                        return x

        print("register not found " +str(input))
        return None

def getRegisterValue(input):
        index = getRegisterPosition(input)
        if index != None :
                return registerValues[index]
        else:
                print("register value couldn't be recovered" + str(input) )

def setRegister(letter, value):
        index = getRegisterPosition(letter)
        registerValues[index] = value

#get the value of an operand which could be a number or register name
def getOperandValue( input ):
        if input.isnumeric() or input[0] == '-' :
                return int( input )

        return int( getRegisterValue( input ))

#apply instructions to registers
running = True
currentIndex = 0
op1 =0
op2 = 0
lastFrequency = -1
while running:
        #print( str(currentIndex) )
        instruction = input[currentIndex].split()
        print( instruction )
        jmp = 1 #value to jump..1 is default, ie just move to next instruction

        #process instructions
        command = instruction[0]
        op1 = instruction[1]
        if command == 'snd':
                lastFrequency = getOperandValue( op1 )
        elif command == 'set':
                op2 = instruction[2]
                if op2.isnumeric():
                        newvalue = op2
                else:
                        newvalue = getRegisterValue(op2)
                setRegister( op1, newvalue )
        elif command == 'add':
                op2 = instruction[2]
                setRegister( op1, ( getOperandValue( op1 ) + getOperandValue( op2 ) ) )
        elif command == 'mul':
                op2 = instruction[2]
                setRegister( op1, ( getOperandValue( op1 ) * getOperandValue( op2 ) ) )
        elif command == 'mod':
                op2 = instruction[2]
                setRegister( op1, ( getOperandValue( op1 ) % getOperandValue( op2 ) ) )
        elif command == 'rcv':
                op1 = getOperandValue( op1 )
                if op1 != 0:
                        print( "last frequency: " + str(lastFrequency) )
                        break
        elif command == 'jgz':
                op1 = getOperandValue( op1 )
                op2 = instruction[2]
                if op1 > 0:
                        jmp = int(op2)

        #move instruction pointer
        currentIndex += jmp

        #finish if index is out of bounds
        if currentIndex >= len(input) or currentIndex < 0:
                running = False


        
print( registerValues )


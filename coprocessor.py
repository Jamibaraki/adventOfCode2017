#Advent of Code 23
# Coprocessor Conflagration

#Adapted from day 18 processor class
class CoProcessor:

        def start(self):
        

                self.registerLetters = 'abcdefgh'
                self.registerLetterLength = len( self.registerLetters )
                self.registerValues = []
                for letter in self.registerLetters:
                        self.registerValues.append( 0 )

                #assign unique processor value to register 'p'
                #self.setRegister( 'p', uniqueValue )
                #self.setRegister( 'a', 1 )
                        

                self.receiveQueue = []
                self.sendQueue = []

                self.isLocked = False
                
                #self.run()
                self.currentIndex = 0

                self.lastFrequency = -1
                
                #file = open('inputTest.txt','r')
                file = open('input23Modified.txt','r')
                self.input = file.read().split('\n')
                file.close()

                self.running = True
                self.multiplyCount = 0
                
                

        def getRegisterPosition(self, input):
                for x in range(0, self.registerLetterLength):
                        if input == self.registerLetters[x]:
                                return x

                print("register not found " +str(input))
                return None

        def getRegisterValue(self, input):
                index = self.getRegisterPosition(input)
                if index != None :
                        return self.registerValues[index]
                else:
                        print("register value couldn't be recovered" + str(input) )

        def setRegister(self, letter, value):
                index = self.getRegisterPosition(letter)
                self.registerValues[index] = value

        #get the value of an operand which could be a number or register name
        def getOperandValue( self, input ):
                if input.isnumeric() or input[0] == '-' :
                        return int( input )

                return int( self.getRegisterValue( input ))

        def processInstruction(self):

                
                
                op1 =0
                op2 = 0
                if self.currentIndex < 0 or self.currentIndex >= len(self.input):
                        running = False
                        return
                
                instruction = self.input[self.currentIndex].split()


                #print( instruction )
                #print ( self.registerValues )
                jmp = 1 #value to jump..1 is default, ie just move to next instruction

                #process instructions
                command = instruction[0]
                op1 = instruction[1]
                if command == 'pass':
                        pass
                elif command == 'set':
                        op2 = instruction[2]
                        if op2.isnumeric():
                                newvalue = op2
                        else:
                                newvalue = self.getRegisterValue(op2)
                        self.setRegister( op1, newvalue )
                elif command == 'add':
                        op2 = instruction[2]
                        self.setRegister( op1, ( self.getOperandValue( op1 ) + self.getOperandValue( op2 ) ) )
                elif command == 'mul':
                        op2 = instruction[2]
                        self.setRegister( op1, ( self.getOperandValue( op1 ) * self.getOperandValue( op2 ) ) )
                        self.multiplyCount +=1
                elif command == 'sub':
                        op2 = instruction[2]
                        self.setRegister( op1, ( self.getOperandValue( op1 ) - self.getOperandValue( op2 ) ) )
                elif command =='jnz':
                        op1 = self.getOperandValue( op1 )
                        op2 = instruction[2]
                        if op1 != 0:
                                jmp = int(op2)

                #move instruction pointer
                self.currentIndex += jmp

                #finish if index is out of bounds
                if self.currentIndex >= len(self.input) or self.currentIndex < 0:
                        self.running = False

                #print( self.currentIndex )
                #print( self.getRegisterValue( 'h' ) )
 
                
        
                 

#Advent of Code 18b
# Duet

class Processor:

        def start(self, uniqueValue):




                self.registerLetters = 'abcdefghijklmnop'
                self.registerLetterLength = len( self.registerLetters )
                self.registerValues = []
                for letter in self.registerLetters:
                        self.registerValues.append( 0 )

                #assign unique processor value to register 'p'
                self.setRegister( 'p', uniqueValue )

                self.receiveQueue = []
                self.sendQueue = []

                self.isLocked = False
                
                #self.run()
                self.currentIndex = 0

                self.lastFrequency = -1
                
                #file = open('inputTest.txt','r')
                file = open('input18.txt','r')
                self.input = file.read().split('\n')
                file.close()

                self.running = True
                self.sendCount = 0
                


                
                #set lock after each instruction

                #unique value per processor - Added

                        

        #let something external grab something from our send queue
        def getFromQueue(self):
                if len( self.sendQueue ) == 0:
                        return None
                return self.sendQueue.pop(0)

        def receiveQueueItem(self,item):
                self.receiveQueue.append(item)
                

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
                if command == 'snd':
                        #lastFrequency = self.getOperandValue( op1 )
                        #print( str(lastFrequency ) )
                        self.sendCount += 1
                        #add this to the queue of outgoing values
                        self.sendQueue.append( self.getOperandValue(op1) )
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
                elif command == 'mod':
                        op2 = instruction[2]
                        self.setRegister( op1, ( self.getOperandValue( op1 ) % self.getOperandValue( op2 ) ) )
                elif command == 'rcv':
                        #op1 = self.getOperandValue( op1 )
                        
                        #if there is something waiting for us go ahead:
                        if len( self.receiveQueue ) > 0:
                                #print(str(len( self.receiveQueue )))
                                self.running = True
                                value = self.receiveQueue.pop(0)
                                #print( str(value) )
                                self.setRegister( op1, value )
                        #otherwise we are stuck waiting.. keep the instruction counter at zero and mark us as waiting
                        else:
                                jmp = 0
                                self.running = False
                elif command == 'jgz':
                        op1 = self.getOperandValue( op1 )
                        op2 = instruction[2]
                        if op1 > 0:
                                op2 = self.getOperandValue( op2 )
                                jmp = int(op2)

                #move instruction pointer
                self.currentIndex += jmp

                #finish if index is out of bounds
                if self.currentIndex >= len(self.input) or self.currentIndex < 0:
                        self.running = False

                
        
                 

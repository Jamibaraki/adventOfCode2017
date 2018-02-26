#Advent of Code 18b
# Duet
#import importlib
#importlib.reload( Processor )
from processor import Processor


print('duet')
processor0 = Processor()
processor1 = Processor()
#processor.run()
processor0.start(0)

processor1.start(1)


running = True

while running:
#for x in range( 0, 10 ):
    #print("t")
    if processor0.running or processor1.running:
        processor0.processInstruction()
        processor1.processInstruction()
    else:
        value = processor0.getFromQueue()
        if value != None:
            processor1.receiveQueueItem(value)

        valueAlt = processor1.getFromQueue()
        if valueAlt != None:
            processor0.receiveQueueItem(valueAlt)

        if value == None and valueAlt == None:
            running = False
            print( str( processor0.currentIndex ) )
            print( str( processor1.currentIndex ) )
            print( processor1.getFromQueue() )
            print( processor0.getFromQueue() )
        else:
            processor0.processInstruction()
            processor1.processInstruction()
            
    #running = False
print("Done!")
print( processor0.registerValues )
print( processor1.registerValues )
print( str( processor1.sendCount ) )

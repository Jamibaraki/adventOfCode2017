#Advent of Code 23a
# Coprocessor Conflagration

#import numpy as np

from coprocessor import CoProcessor
import time
start_time = time.time()
print('Coprocessor Conflagration')

processor = CoProcessor()
processor.start()

while processor.running:
    processor.processInstruction()

print( processor.multiplyCount )

print(time.time() - start_time )

print('finished')





      
    
    





#state = [0,1,2,3,4]
state = [0]
position = 0
#jumps = 3
jumps = 370


#the next value to insert
value = 1

for x in range( 0,2017 ):
#for x in range( 0,2 ):
        #move pointer <jumps number of times>
        position += jumps
        if position >= len(state):
                position = position % len(state)
        #insert the next value
        state.insert(position+1,value)
        position += 1
        value += 1

#print(position)
#print(state)
print(state[position])
print(state[position+1])
print(state[position+2])

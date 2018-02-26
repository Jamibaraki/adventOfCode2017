#Advent of Code 23b
# Coprocessor Conflagration

import time, math
start_time = time.time()

def isPrime( input ):
    #for i in range( 2, math.ceil( ( math.sqrt( input ) ) ) ):
    for i in range( 3, input ):
        if input % i == 0:
            return False
    return True
    #if input != 1:
    #    return True
    #return False

hits = 0
for b in range( 106500, 123501, 17 ):
    if isPrime(b) == False:
        hits += 1

print( hits )

exit()

a = 0
g = 0
h = 0

muls = 0

b = 65          ##set b 65
c = b           ##set c b
if a != 0:       ##jnz a 2
                ##jnz 1 5
    #b *= 100    ##mul b 100
    #b += 100000 ##sub b -100000
    #c = b       ##set c b
    #c += 17000  ##sub c -17000
    f = 1       ##set f 1
    #print( b )
    b = 106500
    c = 123500
    #print( c )
while True:
    print('loop')
    d = 2           ##set d 2
    while True:
        print('loop2' + str(d) )
        e = 2           ##set e 2
        while True:
            #print('loop3'+ str(g) )
            g = d           ##set g d
            g *= e          ##mul g e
            muls += 1
            g -= b          ##sub g b
            if g == 0:      ##jnz g 2
                f = 0       ##set f 0
            e+= 1           ##sub e -1
            g = e           ##set g e
            g -= b          ##sub g b
            if g == 0:
                break ##jnz g -8
        d += 1              ##sub d -1
        g = d               ##set g d
        g -= b              ##sub g b
        if g == 0:          ##jnz g -13
            break
    if f == 0:              ##jnz f 2
        h += 1              ##sub h -1
    g = b                   ##set g b
    g -= c                  ##sub g c
    if g == 0:              ##jnz g 2
        print('exit condition ' + str(muls) ) #3969
        print(time.time() - start_time ) #0.015
        print( h )
        exit()                ##jnz 1 3
    b += 17 ##sub b -17
    ##jnz 1 -23
    #repeat the f = 1 here because the while take us to the middle of an if statement which messes with indentation
    f = 1





      
    
    





#Advent of Code 23b
# Coprocessor Conflagration

a = 0
g=0
h = 0

b = 65          ##set b 65
c = b           ##set c b
if a!= 0:       ##jnz a 2
                ##jnz 1 5
    b *= 100    ##mul b 100
    b += 100000 ##sub b -100000
    c = b       ##set c b
    c += 17000  ##sub c -17000
    f = 1       ##set f 1
while True:
    #print('loop')
    d = 2           ##set d 2
    while True:
        #print('loop2')
        e = 2           ##set e 2
        while True:
            #print('loop3'+ str(g) )
            g = d           ##set g d
            g *= e          ##mul g e
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
        exit                ##jnz 1 3
    b += 17 ##sub b -17
    ##jnz 1 -23
    #repeat the f = 1 here as otherwise the looping doesn't work in python
    f = 1




      
    
    





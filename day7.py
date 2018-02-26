#Recursive Circus
#Advent of Code 2017
#Day 7a
print("reading file")
#file = open('inputTest.txt','r')
file = open('input7.txt','r')
input = file.read()
file.close()

lines = input.split("\n")

#fwft (72) -> ktlj, cntj, xhth


searchnode = 0
found = False

while found != True :
    target = lines[searchnode].split(" ")[0]

    #track searchnode at start of each loop so we can tell if it changes
    initialposition = searchnode
    
    for x in range( 0, len(lines) ):
        if x != searchnode and len(lines[x].split(" ")) > 2:
            parts = lines[x].split(" ")
            for y in range( 3 , len(parts)  ):
                word = parts[y]
                word = word[:-1]
                if word == target:
                    print("found")
                    searchnode = x
                    y = 6
                    x = 50
    #if searchnode hasn't changed after searching we must be at the bottom of the pile
    if( searchnode == initialposition ):
        found = True
        print( target )
                
    

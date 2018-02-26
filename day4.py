#Passphrases
#Advent of Code 2017 Day 4


#deal with the file
file = open('input4.txt','r')
input = file.read()
file.close()

lines = input.split("\n")

validLines = 0

def isValid(line):
    words = line.split(" ")
    #print( str(len(words)))
    for x in range( 0, len(words) ):
        for y in range( x+1, len(words )):
            if( words[x] == words [y] ):
                return False

    return True
                        
                
        

for eachLine in lines:
    if isValid( eachLine ):
        validLines += 1

print('done: ' + str(validLines))
print( str(len(lines)))

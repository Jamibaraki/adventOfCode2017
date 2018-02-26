#Passphrases
#Advent of Code 2017 Day 4b

#exclude anagrams


#deal with the file
file = open('input4.txt','r')
input = file.read()
file.close()

lines = input.split("\n")

validLines = 0

def isAnagram(first, second):
    if( len(first) != len(second) ):
        return False

    for x in range( 0, len(first) ):
        if ( second.find( first[x] ) == -1 ):
            return False
        #if letter was found..remove it from second string
        index = second.find( first[x] )
        newstring = second[:index] + second[(index+1):]
        second = newstring

    return True
        

def isValid(line):
    words = line.split(" ")
    #print( str(len(words)))
    for x in range( 0, len(words) ):
        for y in range( x+1, len(words )):
            if( isAnagram( words[x], words[y] ) ):
                return False

    return True
                        
                
        

for eachLine in lines:
    if isValid( eachLine ):
        validLines += 1

print('done: ' + str(validLines))
print( str(len(lines)))

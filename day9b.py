#Advent of Code '17
#Day 9b - Stream Processing
import sys
print("hello")

#increase recursion limit
sys.setrecursionlimit(2200)

#read input
file = open('input9.txt','r')
input = file.read()
file.close()
#input = "{<a>,<a>,<a>,<a>}"
#input = "{{<!>},{<!>},{<!>},{<a>}}"
#input = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
#input = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
#input = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
#input = "{{!!!}{}}}"
#input = "<random characters>"
#print(input)

#remove cancelled characters from text
#adjusted this due to hitting recursion limit
def pruneCancelled(text):
        count = 0
        hit = False
        for x in range(0,len(text)):
                if x < len( text ):
                        if text[x] == '!':
                                
                                text = text[0:x] + text[x+2:len(text)]
                                return text
        return text

#remove garbage from text
def pruneGarbage(text):
	junkStart = 0
	junkStop = 0
	inJunk = False
	
	for x in range(0, len(text)):
		#print( str(x) + ".." + str(len(text)))
		if x < len(text ):
			if inJunk == False and text[x] == '<':
				junkStart = x
				inJunk = True
			if inJunk and text[x] == '>':
				junkStop = x 	
				text = text[0:junkStart] + text[junkStop+1:len(text)]
				#print("removing " + text + str(junkStart) + " " + str(junkStop))
				inJunk = False
				return text
				
	
	return text

#score groups
def scoreGroups(text):
        score = 0
        level = 0
        for x in range(0,len(text)):
                if x < len(text) :
                        if text[x] == '{':
                                level += 1
                        if text[x] == '}':
                                score += level
                                level -= 1
                        
        return score

#input = pruneCancelled(input)
done = False
while done == False:
        startLength = len(input)
        input = pruneCancelled(input)
        #print( input )
        if len(input) == startLength:
                done = True

#print( "intermediate: " + input )
#input = pruneGarbage(input)
done = False
garbageCount = 0
while done == False:
        startLength = len(input)
        input = pruneGarbage(input)
        if len(input) == startLength:
                done = True
        else:
                garbageCount = garbageCount +  startLength - len(input) - 2
#print( "result: " + input )
score = scoreGroups(input)
print ("score: " + str(score))
print ("Garbage count: " + str(garbageCount))

#count groups
#score groups

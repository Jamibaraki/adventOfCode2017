#Advent of Code 19a
# A Series of Tubes




print('A Series of Tubes')
#file = open('inputTest.txt','r')
file = open('input19.txt','r')
input = file.read().split('\n')
file.close()

#assumption: width/len should be consistent accross input
width = len(input[0] )
height = len(input)

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

passedList = ''

downPipe = '|'
cross = '+'

DOWN = 'd'
UP = 'u'
LEFT = 'l'
RIGHT = 'r'


direction = DOWN
xPos = -1
yPos = -1

print( str( len( input ) ) )
for x in range( 0, width ):
    if input[0][x] == downPipe:
        xPos = x
        yPos = 0
        break

print( str(xPos) + ' ' + str(yPos) )


def run():
    running = True
    while running == True:
        move()
        running = checkSpace()

def checkSpace():
    global xPos, yPos, passedList, direction
    #add to list if in there
    space = input[yPos][xPos]
    #print( space + ' x ' + str(xPos) + ' y ' + str(yPos ) )
    if space == '|' or space == '-':
        pass
    elif space == '+':
        #change direction
        if direction == UP or direction == DOWN:
            if xPos > 0 and input[yPos][xPos-1] != ' ':
                direction = LEFT
            elif xPos < (width-1) and input[yPos][xPos+1] != ' ':
                direction = RIGHT
            else:
                print("couldn't change direction from vertical")
        elif direction == LEFT or direction == RIGHT:
            if yPos > 0 and input[yPos-1][xPos] != ' ':
                direction = UP
            elif yPos < ( height-1) and input[yPos+1][xPos] != ' ':
                direction = DOWN
            else:
                print("couldn't change direction from horizontal")
        else:
            print("couldn't change direction")
        
    elif space in letters:
        #print( 'it was in letters' )
        passedList += space
    elif space == ' ':
        #print( 'it was a space' )
        return False
    return True
    
        

def move():
    global yPos, xPos, direction
    if direction == UP:
        yPos -= 1
    elif direction == DOWN:
        yPos += 1
    elif direction == LEFT:
        xPos -= 1
    elif direction == RIGHT:
        xPos += 1


run()
print("Finished")
print( passedList )


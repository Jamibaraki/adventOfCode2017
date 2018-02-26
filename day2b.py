def find_dividing_numbers(  input ):
    for x in range( 0, len(input) ):
        for y in range( 0,len(input) ):
            if ( x != y ) and ( input[x] > input[y] ) and ( input[x] % input[y] == 0 ):
                return input[x]/input[y]


file = open('input2.txt','r')
input = file.read()


lines = input.split("\n")




sum = 0

for line in lines:
    numbers = line.strip().split("\t")
    
    numbers = [ int(x) for x in numbers ]
    sum += find_dividing_numbers( numbers )


print(sum)

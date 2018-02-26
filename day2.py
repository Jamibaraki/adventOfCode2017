file = open('input2.txt','r')
input = file.read()
#print (input)

lines = input.split("\n")


#print(str(len(lines)))

sum = 0

for line in lines:
    #print(line)
    numbers = line.strip().split("\t")
    
    #print(str(len(numbers))+"****")
    numbers = [ int(x) for x in numbers ]
    sum += (max(numbers)-min(numbers))


print(sum)

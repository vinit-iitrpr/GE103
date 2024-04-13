# opening file as x in reading mode only
x = open("output.txt", "r")
# storing all the lines in lines variable
lines = x.readlines()
# using loop to print line by line
for line in lines:
    # printing line with strip so that the extra line gets removed
    print(line.strip())
    #if there is no line then break
    if not line: 
        break

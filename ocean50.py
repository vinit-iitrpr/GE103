#defining a function for clockwise sense
def clockwise(s):
    #creating an empty string
    t=''
    #creating a dictionary 
    d={'D':'L','L':'U','U':'R','R':'D'}
    for i in s:
        #adding the values in t
        t=t+d[i]
    return t

#defining a function for anticlockwise sense
def anticlockwise(s):
    #creating an empty string
    t=''
    #creating a dictionary
    d={'D':'R','L':'D','U':'L','R':'U'}
    for i in s:
        #adding values in t
        t=t+d[i]
    return t 

#defining a reverse function to reverse the output string
def rev(s):
    t=''
    #creating a dictionary for reverse function
    d={'D':'U','U':'D','R':'L','L':'R'}
    for i in s:
        #adding values in t
        t=t+d[i]
        #returning the reverse of the output
    return t[::-1]

#defining another function block
def block(n):
    if n==1:
        return 'DRU'
    else:
        return rev(anticlockwise(block(n-1))) + 'D' + block(n-1) + 'R' + block(n-1) + 'U' + rev(clockwise(block(n-1)))

#defining ther function for converting the string into coordinates
def s_to_c(s):
    #initially assigning value to x any equals to 1
    x=1
    y=1
    #creating an empty list
    l=[]
    #appending the coordinate (1,1) into list
    l.append((x,y))

    for i in s:
        #if we go downwards increase x by 1
        if i=='D':
            x+=1
            #if we go right increase y by 1
        elif i=='R':
            y+=1
            #if we go left decrease y by 1
        elif i=='L':
            y-=1
            #if we go upwards decrease x by 1
        elif i=='U':
            x-=1
        
        #appending the remaining coordinates into list
        l.append((x,y))

    return l
print(s_to_c(block(int(input("n=")))))
    




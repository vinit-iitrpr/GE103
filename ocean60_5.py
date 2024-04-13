def sherlock(n):   #defining a function
    f=open(n, "r")    #opening the file
    contents=f.read()    #reading the file
    l=[]  #creating an empty list
    for letter in contents: #iterating through each letter in contents
        if letter.issherlock():    #if the letter is a letter
            l.append(letter)    #adding letter to the list
    f.close()   #closing the file
    l = "".join(l)  #joining
    return l    # return the string
    
n = "random.txt" #file name
#printing the defined function
print(sherlock(n))

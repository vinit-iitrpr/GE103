import string

#1st question
def textstrip(filename): #defining a function 
    l = ''  #creating an empty list
    f = open(filename)  #opening file here
    content = f.read() # reading the file
    for letter in content: # iterating over the data
        if letter.islower():    # checking if the letter is lowercase
            l += letter # adding the letter to the string
    return l    # returning the string

# 2nd question
def letter_distribution(s): #defining a function
    d = {}  #craeting an empty dictionary
    for letter in s:    #going over the the argument
        if letter in string.ascii_lowercase:    #checking foe lower case letter
            d[letter] = d.get(letter, 0) + 1    # adding the letter to the dictionary
    return d    #returning dictionary

# 3rd question
def substitution_encrypt(s,d):  #defining a function with s and d as argument
    l = ''  #creating an empty string
    for letter in s:    #going over the string
        if letter in d: # checking if the letter is in the dictionary
            l += d[letter]  # adding the letter to the string
        else:   
            l += letter #adding letter to string
    return l    #returning the string

# 4th question
def substitution_decrypt(s,d): #defining a function with s and d as argument
    l = ''  #creating an empty string
    x = string.ascii_lowercase  #creating a list of lowercase alphabets
    value = list(d.values())    # creating a list of values of the dictionary
    keys = list(d.keys())  # creating a list of keys of the dictionary
    for letter in s:    # going over the string
        if letter in x:     #checking for letters in alphabets
            l += keys[value.index(letter)] # adding the letter to the string
        else:  
            l += letter
    return l    # returning the string

# 5th question
def cryptanalyse_substitution(s): #defining a function
    x = list(string.ascii_lowercase)    # creating a list of alphabets
    l = []
    for letter in x:    # going over the list of alphabets
        l.append([letter, s.count(letter)])    # adding the letter and its count to the list
    l.sort(key = lambda t: t[1], reverse=True)    # sorting the list according to the count of the letters
    # defining a set of substituions
    y = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w', 'g', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z']
    d = {}  # creating an empty dictionary
    for i in x: #applying for loop
        d[i] = l[y.index(i)][0]
    return d #returning the function

# 6th question
def vigenere_encrypt(s,password):   # s is a string and password is a string
    x = list(string.ascii_lowercase)    # creating a list of alphabets
    l = []   #creating an empty list
    for a in password:  #going over the password
        l.append(x.index(a) + 1) # adding the index of the letter to the list
    t = ''   #creating an empty string
    k = 0   #creating variable and assigning its vale to 0
    for letter in s:    #going over the string
        try:    #using try except block to handle the index error
            t += x[x.index(letter) + l[k]]    #adding the letter to the string
        except IndexError:
            t += x[x.index(letter) + l[k] - 26] 
        if k == len(l)-1:    # checking if the index is equal to the length of the list of keys
            k = 0  
        else:
            k += 1  # increase the variable by 1
    return t # returning the string

# 7th question
def vigenere_decrypt(s,password): #defining a function
    x = list(string.ascii_lowercase)    # creating a list of alphabets
    keys = []   #creating an empty list
    for a in password:  #going over the password
        keys.append(x.index(a) + 1) # adding the index of the letter to the list
    t = ''   # creating an empty string
    k = 0   # creating variable for index
    for letter in s:    #going over the string
        try:    # using try except block to handle the index error
            t += x[x.index(letter) - keys[k]]
        except IndexError:
            t += x[x.index(letter) - keys[k] + 26]
        if k == len(keys)-1:    # checking if the index is equal to the length of the list of keys
            k = 0  
        else:
            k += 1  #increase the value of variable by 1
    return t #returning the string

# 8th question
def rotate_compare(s,r):    #defining a function with s as initial string
    x = list(string.ascii_lowercase)    # creating a list of alphabets
    f = '' # creating an empty string for rotation
    for letter in s:   # going over the string
        try:    # using try except block to handle the index error
            f += s[s.index(letter) + r]  # adding the letter to the string
        except:
            f += s[s.index(letter) + r - len(s)]   
    y = 0   #creating a variable and assigning its value to 0
    for i in range(len(s)):    # going over the string
        if s[i] == f[i]:  # checking if the letters are same
            y=y+1  # increase the value of varaible by 1
    return y/len(s)    # returning the count

# 9th question
def cryptanalyse_vigenere_afterlength(s,t):     #defining a function
    x = list(string.ascii_lowercase)    # creating a list of alphabets
    l = []  # initializing an empty list
    for letter in s:    #going over the string
        if letter in list(string.ascii_letters):    # checking if the letter is in the list of alphabets
           l.append(letter.lower()) # adding the letter to the list
    d = {}  # creating an empty dictionary to contain letters
    y = {}  # creating an empty dictionary to store count of letters
    for i in range(t):  # going over the range of k
        d[i] = []   # creating an empty list in ith key of the dictionary
        y[i] = []   # creating an empty list in ith key of the dictionary
    for i in range(len(l)):   # going over the length of the list
        d[i%t].append(l[i]) # adding the letter to the list
    for i in range(t):  # going over the range of k
        for letter in x:    # going over the list of alphabets
            y[i].append([letter, d[i].count(letter)])   # adding the letter and its count to the list
    for i in range(t):  # going over the range of k
        y[i].sort(key = lambda x: x[1])   # sorting the list according to the count of the letters
    lock = ''   # creating an empty string
    for i in range(t):  # going over the range of k
        lock += x[x.index(y[i][-1][0]) - 5]  # adding the letter to the string
    return lock # returning the string
        
# 10th question
def cryptanalyse_vigenere_findlength(s):    #defining a function
    x = list(string.ascii_lowercase)    # creating a list of alphabets
    d = {}  # creating an empty dictionary
    r = 0   # creating a variable
    p = 0 # creating a variable for percentage
    while (p <= 6):   # while the percentage is less than 6
        t = ''   # creating an empty string
        r += 1  # incrementing
        for i in range(len(s)): # going over the string
            # using try except block to handle the index error
            try:
                temp += s[i + r]    # adding the letter to the string
            except: 
                temp += s[i + r - len(s)]   # adding the letter to the string
        c = 0   # creating var for counting
        for i in range(len(s)): # going over the string
            if s[i] == t[i]: # checking if the letters are same
                c += 1  # incrementing
        p = (c/len(s))*100    # calculating the percentage
    return r    # returning the rotation

# 11th question
def cryptanalyse_vigenere(s): #defining a function
    k = cryptanalyse_vigenere_findlength(s)     #finding length of password
    password = cryptanalyse_vigenere_afterlength(s,k)   # finding the password
    t = vigenere_decrypt(s, password)   # decrypt the string
    print("len of password: ", k)    # print the length of the password
    print("password: ", password)   # print the password
    return t    # return the decrypted string
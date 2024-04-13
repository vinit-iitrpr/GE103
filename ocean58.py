def mir(l): #defing a function for mirror image of path
    d = {'u': 'u', 'd': 'd', 'r': 'l', 'l': 'r'} #creating dictionary for replacement
    t = []#creating an empty list
    for i in l:
        t += d[i]#adding elements in list
    return t

def down(l): #defining a function with first letter changed to d
    d = {'u': 'd', 'd': 'u', 'r': 'r', 'l': 'l'}#creating a dictionary for replacement
    t = [] #creating an empty list
    for i in l:
        t += d[i] #adding elements in t
    return t

def path(q): #returing the path of piano curve of order q
    a = ['u', 'r', 'd', 'r', 'u'] 
    t = [] #creating an empty list
    i = 1 #assigning a value to variable
    while i <= q: #upto i<=q
        if i == 1:
            t += a #increase t by a
            i += 1 #increase i by 1
        else:
            f = t + ['u'] + mir(t) + ['u'] + t
            i += 1
            t = f + ['r'] + down(f) + ['r'] + f
    return t
    
def peano(q): #defining a function for peano curve
    direction = path(q)
    d = {'u': (0,1), 'd': (0,-1), 'r': (1,0), 'l': (-1,0)} #creating dictionary for substituent
    t = [(0,0)]
    for i in direction:
        t.append((t[-1][0]+d[i][0], t[-1][1]+d[i][1])) #appending the elements in t
    return t
    

q = int(input("Enter the number: "))
l = ['u', 'r', 'd', 'r', 'u'] #creating a list
n = peano(q)

import matplotlib.pyplot as plt
import numpy as np
# ploting the points
x = np.array([i[0] for i in n])
y = np.array([i[1] for i in n])
plt.plot(x,y)
plt.show()

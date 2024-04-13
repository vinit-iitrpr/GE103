#defining a function find_max with argument L
def find_max(L):
    #assinging the value to a variable
    a=0
    # b is an element of list L
    for b in L:
        if b>a:
            #if b>a it will assign the value of b to a and if not then it will return the previous value of a only
            a=b
    return a
#printing the defined function
print(find_max([13,27,1009,2,20065]))

    
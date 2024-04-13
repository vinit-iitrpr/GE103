def findmedian(l): #defining a function to find median of an unsorted list
    if len(l) & 1:  #for odd number
        return findmidelement(l,(len(l)//2))  #calling dunction to find middle element
    else:
        a = findmidelement(l,(len(l)//2)-1) #to find element before the middle element
        b = findmidelement(l,(len(l)//2)) #to find middle element 
        avg = (a + b)/2 #average of two middle elements in the list
        return avg  #returning the average

def findmidelement(l,x):  #defining a function
    middle=l[0]    # considering the first element of the list as the pivot element
    t1 = [] # list of elements less than the pivot element
    t2 = [] # list of elements greater than the pivot element
    for i in l: #going over the list
        if i < middle:  #if pivot element is greater than element
            t1.append(i)
        elif i > middle: # if element is greater than the pivot element, it is appended to the list of elements greater than the pivot element
            t2.append(i)
    if len(t1)==x:    # if the length of the list of elements less than the pivot element is equal to the given index, then the pivot element is the required element
        return middle  # returns the pivot element
    elif len(t1)+1 > x: 
        return findmidelement(t1,x)   # calls findmidelement function to find the element at the given index in the list of elements which are less than the pivot element
    else:
        return findmidelement(t2, x-len(t1)-1) # if the length of the list of elements is less than the pivot element which are less than the given index then the index is reduced by the length of the list of elements less than the pivot element and 1

w = [3,5,8,11,6,2]
z = [4,5,3,6,2,3,8]
print(f"Median of {w} is {findmedian(w)}")
print(f"Median of {z} is {findmedian(z)}")
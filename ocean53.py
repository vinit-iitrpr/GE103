def swap(a, x, y): #defining a function
    a[x], a[y] = a[y] , a[x] #interchanging the values
    return a

def part(a, low, high): #defining a function
    pindex = low    #starting index as pivot
    pivot = a[pindex]   #storing
    while low < high:   #upto low is less than high
        while low < len(a) and a[low] <= pivot:     #finding element
            low += 1    #increasing the low value by 1
        while a[high] > pivot: #finding element
            high -= 1   #decreasing the high value by 1
        if low < high:  #swapping high and low position
            a = swap(a, low, high)
    a = swap(a,high,pindex) #swapping piivot element 
    return pindex   #returning

def quicksort(a, low, high):   #defining main function
    if low < high:  #upto low is equal to high
        pindex = part(a,low, high)  #using part to get partion index
        #using recurssion
        a = quicksort(a, low, pindex-1)
        a = quicksort(a, pindex+1, high)
    return a #returing list after sorting

a = [3, 2, 1, 5, 4] #sorting
print("unsorted list:",a) #printing unsorted list
print("sorted list:",quicksort(a,0,len(a)-1)) #printing sorted list

#defining a function for binary search and key is one element in list which we are searching
def binary_search(list1,key):
    #assigning value to lower index as 0
    low=0
    #assigning value to higher index as len(list1)-1
    high=len(list1) - 1
    #defining a variable called "found" assigning it's initial value as false
    found=False

    #running while loop till lower index is smaller than higher index and our "found" variable gets value as true
    while(low<=high and not found):
        #middle index will be GIF of average of lower and higher indices
        mid=(low+high)//2
        #if key is our middle index element of list
        if(key==list1[mid]):
            #variable takes value as true
            found=True
            #if key is greater than middle index element
        elif(key>list1[mid]):
            #will remove the left side of list including the middle element and our new lower index becomes middle index + 1
            low=mid + 1
            #if key is smaller than middle index element of list
        else:
            #remove the right side of list and our new higher index becomes middle index - 1
            high=mid - 1

    if(found==True):
        print("Key is found")
    else:
        print("Key is not found")

#craeting an unsorted list
list1=[23,1,4,2,3]
#sorting the unsorted list
list1.sort()
#searching for element 2 in list1
binary_search(list1,2)

#defining the function called mergesort
def mergesort(list1):
    #when len(list1)>1
    if len(list1)>1:
        #middle element will be GIF of len(list1)/2
        mid=len(list1)//2
        #left_list is the left list after splitting
        left_list=list1[:mid]
        #right_list is the right list after splitting
        right_list=list1[mid:]
        #applying recurssion for right_list
        right_list = mergesort(right_list)
        #applying recurssion for left_list
        left_list = mergesort(left_list)
        #variable for index of left_list
        i=0
        #variable for index of right_list
        j=0
        #variable for index of new list1 in which we are finally sorting the elements
        k=0    

        #upto i<len(left_list) and j<len(right_list)
        while(i<len(left_list) and j<len(right_list)):
            #if ith element of left list is less than jth element of right list
            if(left_list[i]<right_list[j]):
                #assign kth element of list1 to ith element of left list
                list1[k]=left_list[i]
                #increasing the value of i by 1
                i=i+1
                #increasing the value of k by 1
                k=k+1

            else:
                #assign kth element of list1 to jth element of right list
                list1[k]=right_list[j]
                #increase the value of j by 1
                j=j+1
                #increase the value of k by 1
                k=k+1
        
        #if all the elements of right list gets appended
        while(len(left_list)>i):
            #then drop all the remaining elements of left list to list1
            list1[k]=left_list[i]
            #incraese i by 1
            i=i+1
            #increase k by 1
            k=k+1

        #if all the elements of left list gets appended
        while(len(right_list)>j):
            #then drop all the remaining elements of right list to list1
            list1[k]=right_list[j]
            #increase j by 1
            j=j+1
            #increase j by 1
            k=k+1
    
    #returning the defined function
    return list1


#giving input of list
list1=[20,1,50,40,10]
#printing the defined function
print(mergesort(list1))      

    
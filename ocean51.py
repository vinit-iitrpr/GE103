#creating a non empty list
list=[10,15,4,23,0]

#first printing the unsorted list
print("unsorted list=",list)

#applying this for loop for number of passes or itieration we want to do in program
for i in range(len(list)-1):
    #applying this for loop for no. of iteration we want to do in given list
    for j in range(len(list)-1):
        #if preceding element in list is greater than the succeding element 
        if(list[j]>list[j+1]):
            #then swap the elements
            list[j],list[j+1] = list[j+1],list[j]

#printing the sorted list
print("sorted list=",list)
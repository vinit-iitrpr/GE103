#importing library of time
import time
#importing the files of buuble, merge, quick sort
import ocean51
import ocean52
import ocean53

#opening the file with one word per line
with open('english_random.txt') as f:
    alpha = (f.readlines())
#removing new line character
alpha = [i.strip() for i in alpha]

#starting the time
starttime = time.time()
d = {}

#using quick sort
a = ocean53.quicksort(alpha, 0, len(alpha)-1)
d['quicksort'] = time.time() - starttime  #time taken by quick sort

#using merge sort
b = ocean52.mergesort(alpha)
d['mergesort'] = time.time() - starttime  #time taken by merge sort

#using bubble sort
c = ocean51.bubblesort(alpha)
d['bubblesort'] = time.time() - starttime

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
d['bubblesort'] = time.time() - starttime #time taken by bubble sort

#printing the lists that we have sorted
print("Merge Sort: ", b, "\n")
print("Quick Sort: ", a, "\n")
print("Bubble Sort: ", c, "\n")

# printing the time taken by each algorithm
print("time taken by each algorithm is: ", d)
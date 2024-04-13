def contigious_subarray(l): #defining a function for maximum sum in contigious sub array
    i = 0   #i is the startpoin tof sub array
    j = 0   #j is the end point of sub array
    maximumsum = (0, 0, 0) #maximum sum is a tuple
    while i < len(l):   #applying while loop upto i<len(l)
        j = i  
        sum = 0 
        while j < len(l):   #applying while loop upto j<len(l)
            sum += l[j]    #adding elements to the variable
            if sum > maximumsum[0]:    #if sum>maximum sum
                maximumsum = (sum,i,j) #replacing the maximum sum
            j += 1  #increasing j by 1
        i += 1  #increasing i by 1
    return l[maximumsum[1]:maximumsum[2]+1]

l = [-2, 1, -3, 4, -1, 2, 1, -5, 4] #given a list
print(l) #printing the list
print(contigious_subarray(l))#printing the function with removing next line space
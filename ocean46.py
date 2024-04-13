#defining the function for sum of matrices A and B
def sum(A,B):
    #creating empty list 
    c=[]
    
    for i in range(len(A)):
       #creating empty list for row
        row=[]
        for j in range(len(A)):
            #appending the sum of i and j in row list
             row.append(A[i][j] + B[i][j])
       #appending the row list into empty c list
        c.append(row)

    return c

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[11,12,13],[14,15,16],[17,18,19]]

print(sum(a,b))


                   


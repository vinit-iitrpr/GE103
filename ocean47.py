#defining a function for pdt of two matrices
def pdt(a,b):
    r=len(a)
    #creating an empty list to store the product of matrices
    pdt=[]

    for i in range(r):

        #storing the ith row in variable called row
        row=a[i]

        #creating empty list to store 1 row of pdt matrix
        p_row=[]

        #checking through the coloumns of matrix b
        for j in range(r):
            
            s=0

            #checking through the ith row of a and jth column of b
            for k in range(r):  

                #variable 's' is used to store the sum of pdts of elements of ith row of a and jth column of b
                s+=row[k]*b[k][j]

            #appending the sum the the list p_row
            p_row.append(s)

        #appending p_row to pdt list
        pdt.append(p_row)

    return pdt

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[10,10,10],[10,10,10],[10,10,10]]

print(pdt(a,b))

        

              


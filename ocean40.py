#creating a list of alphabets used in series
L= ["R", "U", "L", "D"]
#generating two variables and assigning them values
n=1
m=0

#aapplying while loop
while m<1000000:

    #appling this for loop for R and U
    for i in range(0,2):
        for k in range(n):
            print(L[i], end=" ")

    #everytime m increases to 2 raise to the power like function
    m=m+2*n
    n=n+1

    #applying this for loop for U and D
    for i in range(2,4):
        for k in range(n):
            print(L[i], end=" ")

    #here also m increases to 2 raise to the power like function
    m=m+2*n
    n=n+1
import random 
#taking input from the user for no. of bins wants to be stimulated
n=int(input("enter the number of bins to be simulated:"))

#creating empty list to store the no. of balls in each bin
L=[0]*n

x=0

#add 1 ball to random bin until all bins have atleast 1 ball in them
while 0 in L:
    #incraese x by 1
    x+=1
    #add 1 ball to random bin
    L[random.randint(0,n-1)]+=1

print(L)
print(x, "Balls were thrown")
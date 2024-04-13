#applying import random function to randomly distribute n balls into n bins
import random 
#taking input from the user for no. of balls and bins to be stimulated
n=int(input("how many balls and bins wants to be stimulated:"))

#creating n empty bins
L=[0]*n

for i in range (n):
    #increase the number of balls by 1 in that bin if the ball is thrown in it
    L[random.randint(0,n-1)]+=1
#printing L
print(L)
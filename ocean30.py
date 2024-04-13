#in euclidian algorithm to calculate gcd of 2 numbers fibonacci numbers take maximum number of steps
#defining a function to calculate nth fibonacci number
def fib(n):
    #we need to return first two fibonacci numbers
    if(n==1):
        return 0
    elif(n==2):
        return 1
    #we know that in fibonacci series every term is sum of it's previous two terms
    else:
        return fib(n-2) + fib(n-1)

k=int(input("enter the number of digits:")) 
#defining a variable to check values of fibonacci series   
i=0
#defining a variable to break the while loop if it exceeds the number of digit which we entered
a=1
#defining while loop to check the number of fibonacci terms in that given range
while(a<10**k):
    #increasing the value of i by 1 everytime after checking every fibonacci number
    i+=1
    #assigning the value of fibonacci number to 'a'
    a=fib(i+1)
#printing the last two fibonacci number in that given range of digits
print(fib(i),fib(i-1))
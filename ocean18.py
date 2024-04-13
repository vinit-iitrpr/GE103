def fib(a):
    if(a==1 or a==2): 
        return 1 # as 1 and 2 term of fibonacci are 1 
    else:
        x = fib(a-1) + fib(a-2) # using recurrence to get nth term of fibonacci sequence
        return x

n = int(input("n = "))

for i in range(1,n+1):
    print(fib(i)) # using loop to print the fib sequence upto n terms

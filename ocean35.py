#defining a function fibonacci(n)
def fibonacci(n):
    #returing the first term of fibonacci sequence
    if n==1:
        return 0
    #returning the second term of fibonacci sequence
    elif n==2:
        return 1
    #every term is the sum of it's previous two terms
    else:
        x = fibonacci(n-1) + fibonacci (n-2)
        
        return x
#taking input from the user 
n=int(input("enter the number:"))
#printing the defined function
print(fibonacci(n))

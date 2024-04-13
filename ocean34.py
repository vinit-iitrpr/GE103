#defining a function factorial(n)
def factorial(n):
    #taking the intial value of variable equals to 1
    x=1
    
    for i in range(1,n+1):
        x*=i
        #returing the factorial of n
    return x
     
n=int(input("enter the number:"))
#printing the factorial of n
print(factorial(n))

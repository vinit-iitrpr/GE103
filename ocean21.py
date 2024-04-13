n = int(input("enter any number:"))
x = 1
for i in range(1,n+1):
    #we need to multiply upto and including n
    x *= i 
print(f"factorial of n is {x}")
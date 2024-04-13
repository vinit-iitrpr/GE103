n=int(input("enter the value of n:"))

for i in range(2,n):
    d= n/i
    g= n//i
    f= d- g
    if(f==0):
        break
    else:
        continue
if(n==0 or n==1):
    print("n is not a prime number")
elif(f==0):
    print("n is not a prime number")
else:
    print("n is a prime number")


n = int(input("enter the value of n: "))

for i in range(2,n+1):
    a = 0
    for m in range(2,i):
        d = i/m
        g = i//m
        f = d - g
        if f==0:
            a += 1
            break
        else:
            pass
    if a==0:
        print(i)
    else:
        pass

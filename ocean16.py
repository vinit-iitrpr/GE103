n=input("enter a string:")
v=0
c=0
for i in n:
    if i in "aeiou":
        v+=1
    elif i in "bcdfghjklmnpqrstvwxyz":
        c+=1
print(v)
print(c)


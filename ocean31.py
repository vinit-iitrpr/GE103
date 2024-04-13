#creating an empty list so that we can fill it
l = [] 
n = int(input("enter the number:"))
# using loop to append all the natural numbers upto n
for i in range(1,n+1):
    l.append(i)

print(l)
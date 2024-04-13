import random
n=int(input("enter how many number you want to add in list l:"))
l=[]
#using for loop to append n random numbers
for i in range(n):
    l.append(random.randint(1,1000))
#printing n diffrent random numbers in the range (1,1000)
    
print(l)
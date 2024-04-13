n = int(input("Enter the number: "))
l = [] 
#creating empty list to add the bits of binary number
#creating while loop to continue adding remainder of n/2 until quotient(n//2) comes out to be 0
while n != 0:
    l.append(n%2)
    n = n//2
#using for loop and negative indexing to reverse the order of elements and print them one after the other
for i in range(1,len(l)+1):
    print(l[-i], end="")

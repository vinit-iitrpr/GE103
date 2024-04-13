#defining a function is_even
def is_even(n):
    #if reaminder comes out to be zero after dividing by 2
    if n%2==0:
        return True   
    else:
        return False
#taking input from the user        
n=int(input("enter the number:"))
#printing the defined function
print(is_even(n))
    
   
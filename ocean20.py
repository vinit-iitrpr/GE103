#taking input for lines and curvature
n=int(input("enter the number of lines:"))
c=int(float(input("enter the curvature:"))*10)
#if curvature is positive parabola will be opening rightwards
if(c>0):
    for i in range(1,n+1):
        #this will print star from n/2 lines to -n/2 lines
        y=int((1+n)//2 - i)
        x=y**2
        #this will shift the stars in proper line up
        print(" " * x * c + "*")
#for negative curvature parabola will open leftwards
else:
    for i in range(1,n+1):
        y=int((1+n)//2 - i)
        #this will subratact the maximum value of x from y**2
        x=((n+1)//2 - 1)**2-y**2
        #the curavture is neagtive that's why multiply by -c'
        print(" " * x * -c + "*")
    
    
    

   
    
    
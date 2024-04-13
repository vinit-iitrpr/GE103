#defining a function circle_area with argument as r
def circle_area(r):

    #importing math as m to use the the value of pi
    import math as x
    #using the formula of area of circle
    A = x.pi*(r**2)
    #returing the area of circle
    return A
#taking input from the user for value of radius
r=float(input("enter the radius:"))
#printing the function circle_area(r)
print(circle_area(r))
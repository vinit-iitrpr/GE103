#first we need to enter the marks in all 5 subjects
a=int(input("enter the marks in subA:"))
b=int(input("enter the marks in subB:"))
c=int(input("enter the marks in subC:"))
d=int(input("enter the marks in subD:"))
e=int(input("enter the marks in subD:"))
#average is being taken
f=(a+b+c+d+e)/5
#writting conditions for A,B,C,D and F grade
if(f>=90):
	print("A")
if(f<90 and f>=80):
	print("B")
if(f<80 and f>=70):
	print("C")
if(f<70 and f>=60):
	print("D")
if(f<60):
	print("F")

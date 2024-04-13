y = int(input("enter the year: "))

# checking if the year is leap or not
#if years(not including 100's check divisiblity by 4)
#if years in 100's then check divisiblity by 100 as well as 400
if y%400==0:
    print(f"{y} is a leap year")
elif y%100 !=0 and y%4==0:
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")

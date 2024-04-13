#applying this to find unit of temperature
#f stoods for fahrenhite
#c stoods for celcius
temp=input("for c to f conversion press a and for f to c conversion press b:")
#applying this to take input of temp
n=float(input("enter the temperature:"))

# if temp is in celcius
if temp=="a":
    #formula for c to f conversion
    f=(n*(9/5))+32
    print(f)
#if temp is in fahrenhite
else:    
    #formula for f to c conversion
    c=(n-32)*5/9
    print(c)
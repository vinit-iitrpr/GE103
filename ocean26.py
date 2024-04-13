n = int(input("enter the number: "))

# if remainder of n/7 and n/5 is zero then it is divisble by both
if(n%7==0 and n%5==0):
    print(f"{n} is divisible by both 7 and 5")
else:
    print(f"{n} is not divisible by both 7 and 5")
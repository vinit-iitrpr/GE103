# taking input from the user
n = int(input("Enter the number: "))
# using with to open file as f
with open("output.txt", "w") as f:
    # using for loop to take all natural numbers upto n
    for i in range(1,n+1):
        # writing the numbers one by one in the file which is opened by f
        f.write(f"{i}\n")


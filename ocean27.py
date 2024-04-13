age=int(input("enter your age:"))
#using inequalities to categorize the age's'
if(age<18):
    print("you are a minor")
elif(18<=age<65):
    print("you are an adult")
else:
    print("you are a senior citizen")
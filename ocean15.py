a=input("enter any word:")
#first : is used to tell from where we need to start
#second : is used to tell to where we need to end
b=a[::-1]
#this means a is equivalent to b
if a==b:
    print("a is a palindrome")
else:
    print("a is not a palindrome") 
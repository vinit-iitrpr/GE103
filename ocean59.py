#input for message
message=str(input("enter the string:"))
#input for shifting of original position
key=int(input("enter the key:"))

#giving an alphabet string
alphabet="abcdefghijklmnopqrstuvwxyz"
#creating the empty string to store the encrypted string
encrypt=""
#applying for loop to iterate through the given message
for i in message:
    #finding the indices of alphabets
    position=alphabet.find(i)
    ##new position will be original position + key given
    new_position=position + key
    #storing the encrypted string into empty string
    encrypt+=alphabet[new_position]

#printing the encrypted string
print(encrypt)
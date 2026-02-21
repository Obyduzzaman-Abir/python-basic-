#basic string
a= "Haary Potter and the Goblet of Fire"
print (a)

#To Find the length
print (len(a))

# to find the number of times a character is occuring
print (a.count("o"))

#to convert each letter into upper case
print(a.upper())

#to convert each letter into lower case
print(a.lower())

#find any character index
print(a.find("o"))
#find index in range
print(a.find("o",15,34))

# to convert the fist latter to capital
print(a.capitalize())

# to convert string into lower case
print(a.casefold())

#to find the index number of a character

print(a.find("o",15,25))

name= "john"
b ="my name is " , name
print(b)
b1="My name is {}".format(name)
print(b1.format(name))

#it fills the given characters and centralizes a string
print(name.center(10,"*"))

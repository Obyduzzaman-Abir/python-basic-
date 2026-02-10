# #write a program check whether the passed letter is a vowel or not
# letter =input("Enter a letter: ")
# if (letter in "aeiou") or (letter in "AEIOU") :
#     print(letter + " " + "Is a vowel")
# else:
#     print(letter + " "+ "is not a vowel")

#check the number of digit of a numbers

num=int(input("Enter a number upto 5 didits : "))
if num>=0 and num<=9:
    print("It is a single digit number")
elif num>=10 and num<=99:
    print("It is an two digit number")
elif num>=100 and num<=999:
    print("It is a three digit number")
elif num>=1000 and num<=9999:
    print("It is a four digit number")
else:
    print("It is a five digit number")

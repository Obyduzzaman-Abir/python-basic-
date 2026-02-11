#Basic while loop
from itertools import repeat

n =1
while n<=5:
    print (n)
    n+=1

#Table of n
n1=1
a =7
while n1<=10:
    print (a,"*", n1 ,"=", n1*a)
    n1+=1

#True statement is while
while True:
    num1=int(input("Enter a number1: "))
    num2=int(input("Enter a number2: "))
    print (num1+num2)
    repeat= input("Would you like to continue (yes/no): ")
    if repeat=="yes":
        break
    else:
        continue



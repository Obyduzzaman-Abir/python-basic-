# #Write a program to check if a number is positive
# num =int(input("Enter a number"))
# if num>0 :
#     print("The number is positive")
# elif num<0:
#     print("The number is negative")
# else:
#     print("The number is zero")
#
#
# #Write a program to know number odd or even
# num1=int(input("Enter a number"))
# if num%2==0:
#     print("The number is odd")
# else:
#     print("The number is even")
import math
from operator import length_hint

#Create an area Calculator

choice = int(input ("Enter your choice 1 to 4 "))
if choice==1:
    side = float(input("Enter the length of one side"))
    area=side**2
    print("The area of the square is",area)

elif choice==2:
         length = float(input("Enter the length of the rectangle"))
         width = float(input("Enter the width of the rectangle"))
         area=length*width
         print("The area of the rectangle is",area)
elif choice==3:
       radius=float(input("Enter the radius of the circle"))
       area = math.pi*radius**2
       print("The area of the circle is",area)


elif choice==4:
    base=float(input("Enter the base of the triangle"))
    hight=float(input("Enter the height of the triangle"))
    area=0.5*(base*hight)
    print("The area of the triangle is",area)

else:
    print("Invalid choice")
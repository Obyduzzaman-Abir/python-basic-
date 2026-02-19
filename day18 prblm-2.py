for i in range(1,21):
    print("The first" ,i, " numbers are :" , i , "Squres are : " ,i*i)

sum = 0
n =0
while n<20:
    if n%2 !=0:
        sum = sum + n
    n=n+1
print("all 10 odd ",sum)
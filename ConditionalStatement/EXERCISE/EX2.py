# WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))

if (num1 > num2 and num1 > num3):
    print (num1 , " is grater")
elif(num2 >num3):
    print(num2 , "is grater")
else:
    print(num3 , "is grater")
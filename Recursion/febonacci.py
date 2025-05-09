# f(0) = , f(1) = 1 ;

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("enter the value of n")
n = int(input())
print ("factorial of ", n , "is - " , fibonacci(n))

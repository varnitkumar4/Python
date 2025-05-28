# WAF to find the factorial of n. (n is the parameter)
def fact(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    print(fac)


a = int(input("enter the number to find factorial"))
fact(a)
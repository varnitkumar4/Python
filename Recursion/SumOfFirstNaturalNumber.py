# Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n

a=sum(5)
print(a)  
    
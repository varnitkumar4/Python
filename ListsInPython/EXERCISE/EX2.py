# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

lis1 = ["racecare"]
lis2 = lis1.copy()
lis2.reverse()
print(lis2)

if(lis1 == lis2):
    print("yes, is palindrome")
else:
    print("not, palindrome")
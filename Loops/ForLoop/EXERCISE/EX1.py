# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
y = int(input("enter the val"))
for val in tup:
    if(val == y):
        print("yes")
        
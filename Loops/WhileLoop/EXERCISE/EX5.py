# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
y = int(input("(1, 4, 9, 16, 25, 36, 49, 64, 81, 100), input in this tuple"))
i =0 
while i < len(x):
    if (x[i] == y):
        print("yes")
    i += 1

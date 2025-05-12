x = 10 

def my():

    global x   # function se ham globle x ka value change kar rahe hai 
    x = 5

    y = 6     # ye local variable hai isko ham sirf function ke andar hi use kar sakte hai 
    print(y)

my()
print(x)

#print(y)  y local variable hai is liye usko ham yha print nahi kar sakte hai 
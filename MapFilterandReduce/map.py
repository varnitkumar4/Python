def cube(x):
    return x*x*x

#print(cube(3))

l =[1,2,3,4,5]
# g=[]
# for i in l:
#     g = (cube(i))
#     print(g)

l2 = list(map(cube , l))
print(l2)
# filter matlab filter kar ke dega matlab jo hamko chahiye usi ke hisab se dega
def filter_function(x):
    return x>5
l = [1,2,3,4,5,6,7,8,9]

newl = list(filter(filter_function , l))
print (newl)
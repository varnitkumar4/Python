from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)  # reduce karta hai 

# Print the sum
print(sum)
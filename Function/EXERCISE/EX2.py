# WAF to print the elements of a list in a single line. ( list is the parameter)

fruits = ["apple" , "orange" , "banana", "guva" , "pineapple"]
def print_list(list):
    for item in list:
        print(item , end=" ")

print_list(fruits)
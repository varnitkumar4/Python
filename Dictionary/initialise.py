info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 

# print(info['name'])       # ye agar nahi mila to error through karta hai 
# print(info.get("name"))   # our is me error through nhi karta hai
# print(info.get("age"))
print(info.values())

print(info.keys())  # sara key ek bar me acces kar sakte hai

for key in info.keys():
    print(info[key])
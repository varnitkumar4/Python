# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) & don’t allow duplicate keys
info = {'name':'Karan', 'age':19, 'eligible':True, "sex" : "male"}
print(info) 

# print(info['name'])       # ye agar nahi mila to error through karta hai 
# print(info.get("name"))   # our is me error through nhi karta hai
# print(info.get("age"))


# print(info.values())

# print(info.keys())  # sara key ek bar me acces kar sakte hai

# for key in info.keys():
#     print(info[key])
info["name"] = "raja"   #name change ho gya
# print(info["name"])
# print(info["sex"])
# print(info.keys())
print(list(info.keys()))   # typecasting into list
print(tuple(info.keys()))  # typecasting into tuple
print(len(info))   # length of dect

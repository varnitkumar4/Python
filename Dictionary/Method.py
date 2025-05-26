dec1 = {456:67 , 457:78 , 222:78 , 444:89 , 589:76}
dec2 = {999: 98 , 345: 45}
print (dec1 , dec2)

# dec1.update(dec2)
# print (dec1)

# dec1.pop(222)  # is me jo likhnge usi ko pop karega
# print(dec1)

dec1.popitem()
print (dec1)   # is me jo last me hoga usko pop karega 
print(dec1.values())   # isme sirf value hoga 
print(dec1.items())        # ye key our value dono deta hai
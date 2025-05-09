s1 = {5,6,7,8}
s2 = {10,9,4}

# print (s1.union(s2))   # dono me jo jo number hoga sab , bas jo repit nahi ho 
# #print (s1 , s2)   # ise alag alag set print hoga 

# s1.update(s2)
# print (s1 , s2) # is me huaa ki , ho value s2 me hia o ab s1 me bhi hoga same chor ke 

# s2.update(s1)
# print (s1 , s2) # is me s1 bala sara value s2 me update ho jayega


# #   INTERSECTION

# print(s1.intersection(s2))

#            symmetric_difference

# print(s1.symmetric_difference(s2))  # dono me jo common na ho 

# print(s1.difference(s2))  #in this case output is {5,7} s1 me ho par s2 me na ho, s1 pahle hai is liye usi ka coomon dekha jayega 

# print(s1.issubset(s2))  #false q ki luvh commonni hai ,,, matlab s1 jo hai kya o sub set hai s2 ka 

# print(s1.isdisjoint(s2))  #iksa matlab dono set me comon na ho to output true aayega 


#    ADD

s1.add(0)
print (s1)


# ek remove or discard method v hota hai jo ki set se koi ek string/number delete karta hia
# dono ek difference hota hai delete erro through karta hai matlab jaha error hoga use aage ka code nahi run hoga 
# par dicard error thopugh nahi karta hai ,,is me use aage ka line run hoga 

#  POP()

S = s1.pop()   # koi bhi number pop ho skta hai
print (S)


# NOTE string are immutable (matlab chane nahi hoga)
name = "Rajaram"
print (len(name))
print (name)
print(name.upper())   # NOTE origanal string change nahi hoga  copy change hoga
print(name.lower())  

name2 = "!!shyamnandan!!!!!!!!!!!!!"
print (name2.rstrip("!"))  # rstrip use to remove ! (par jo bad me laga hoga wahi hatega pahle bala nahi)
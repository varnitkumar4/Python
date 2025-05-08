product = ["carPart" , "bickPart" , "bcycle" , "auto","moto","toto"]
print (product)

if "carPart" in product:
    print ("yes")
else:
    print("no")

# if "car" in "carPart":
#     print("Yes")
# else :
#     print ("No")

print(product[:])   # starting se ending tak print karega
print(product[1:3])  # index one se three tak print karega 
print(product[0:6:2]) # start hoga zero se end hoga six par OR do ke addition me chalega like.. 0+2=2 , 2+2=4 , 4+2=6

#            LIST COMPREHENSION

les = [i for i in range(20)]
print (les)

les1 = [i for i in range(20) if i%2 == 0]
print (les1)
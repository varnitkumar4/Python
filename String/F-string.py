# # important 

letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Harry"

print(letter.format(country, name))  #  {1} or {0} kar do to sahi print hoga // string formating me ye ek diadvantage hai 

# after using f-string 

print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")   # do bar {{}} ye lagane pe same chig output me aayega 
price = 49.09999
txt = f"For only {price:.2f} dollars!"  # 2f ka use - desimal ke bad two digit lane ke liye
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))










    

    






















































































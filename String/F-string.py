# important 

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

# after using f-string 

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")   # do bar {{}} ye lagane pe same chig output me aayega 
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))

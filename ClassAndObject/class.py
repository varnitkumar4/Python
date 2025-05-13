class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()
d = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

c.name = "ram"
c.occupation = "god"

# print(a.name, a.occupation)
a.info()    
b.info()
c.info()
d.info()

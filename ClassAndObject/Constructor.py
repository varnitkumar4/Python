class Person:

  def __init__(self, name, occ):   # Constructor ayeshe banta hai (__init__)
    #print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
c = Person("raj" , "Helper")
a.info()
b.info()
c.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()

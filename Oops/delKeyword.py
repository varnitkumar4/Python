# del keyword is use to delete to object properties or object its self

class student:
    def __init__(self , name):
        self.name = name


s = student("raj")
print(s)
print(s.name)

del s.name
print(s.name)  # delet hogya to access nahi kar sakte hai 
        
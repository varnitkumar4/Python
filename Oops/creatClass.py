# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
class student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print(self.name, "your avf score is ", sum/3)
        
s1 = student("ram" ,[4,5,6])
s1.avg()

s1.name="raju"
s1.avg()

s2 = student("kisor" , [8,9,6])
s2.avg()
# inharit karna 
# THREE TYPE OF INHERITANCE 
# 1 - Single-level 
# 2 - multi-level
# 3 - multiple inharetance

class car:

    @staticmethod
    def start():
        print("car is started")
    
    @staticmethod
    def stop():
        print("car is stop")

class toyotacar(car):   # inharit kar rha hia car ki property ko
    def __init__(self, name):
        self.name = name

car1 = toyotacar("s11")
print(car1.name)
print(car1.start())  # inharit kar rha hai car ki property ko phir output de rha hai
print(car1.stop())

car2 = toyotacar("s12")
print(car2.name)
print(car2.start())
        
# agar kisi ko privet banana hai to ha double underscore ka use karte hai 

class accounr:
    def __init__(self, acc_num):
        self.__acc_num = acc_num     #__ iske karan ye private ho gya our isko class se bahar use nahi kar sakte hai 
                                     # iso sirf class ke andar hi use kar sakte hai 

s = accounr(123)
print(s.__acc_num) # yha error dega
         
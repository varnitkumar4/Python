# f = open('FileHandling/myfile.txt' , 'r')
# text = f.read()
# print (text)
# f.close()



# f = open('FileHandling/myfile.txt' , 'w')
# f.write("jay ho")  # jao ho likha gaya hoga pahle bala hat ke 
# f.close()

with open('FileHandling/myfile.txt' , 'a') as f:  # with ka use karenge to hamko close nahi karna parega
    f.write(' sita ram')  # jitana bar isko run karenge utna bar ye add hote rahega us file me
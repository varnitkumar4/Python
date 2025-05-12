f =open('FileHandling/myfile2.txt' , 'r')
while True:
    text = f.readline()
    if not text:
        break
    print (text)
     
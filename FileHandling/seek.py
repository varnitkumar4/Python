# with open('FileHandling/myfile3.txt' , 'r') as f:
#     f.seek(10)              #10bite aage kar dega wha se counting start hoga iska matlab 10 number ke bad 5 number lega
#     data = f.read(5)
#     print(data)


 #             TELL

with open('FileHandling/myfile3.txt' , 'r') as f:
    f.seek(10)              #10bite aage kar dega wha se counting start hoga iska matlab 10 number ke bad 5 number lega
    
    print(f.tell())  # tell batayega ki kha tak seek huaa hai 
    data = f.read(5)
    print(data)

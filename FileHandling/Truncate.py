with open('FileHandling/sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(7)            # ye write karne me madat karega ki kitna hamko likhna hai 

with open('FileHandling/sample.txt', 'r') as f:
  print(f.read())
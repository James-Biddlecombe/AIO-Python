
#file modes
#r - read
#r+ read/write
#a - append
#w - write
#x - create
#t - text
#b - binary

f = open('Topics\Files\quotes.txt')
filecontents = f.read()
print(filecontents)
f.close()
print('File is closed: ', f.closed)
print("Done")

#contextual syntax - no close required
with open('Topics\Files\quotes.txt') as f:
    filecontents = f.read()
    print(filecontents)
print('File is closed: ', f.closed)
print("Done")

#reading binary files (image file)
with open('Topics\Files\happy_pickle.jpg', 'rb') as f:
    filecontents = f.read(100) #read only 100 binary characters
    print(filecontents)
print("Done")

#reading file with encoding utf-8
with open('Topics\Files\\names.txt', 'r',encoding='utf-8') as f:
    current = f.read()
    print(current)
print("Done")

#looping through a files

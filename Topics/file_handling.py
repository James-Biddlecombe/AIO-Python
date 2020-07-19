
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
with open('Topics\Files\quotes.txt') as f:
    #read in all lines in one go then loop through
    for one_line in f.readlines():
        #without the end='' there would be double spaces for new lines and print
        print(one_line,end='')
print()
print("Done")

#looping through with enumerate
#### with enumberate, [0] contains the number of the line
#### whereas [1] contains the its content
with open('Topics\Files\quotes.txt') as f:
    #loop through enumerating
    for one_line in enumerate(f.readlines()):
        #if counter is even number, print with no extra newline
        if one_line[0] % 2 == 0:
            print(one_line[1],end='')
        #otherwise print a couple spaces and an extra newline
        else:
            print('   ' + one_line[1])
print()
print("Done")

#looping with readline
#### readline is used when the size of file is large or unknown
#### this way RAM is not filled and app hung because of a single 
counter = 1
with open('Topics\Files\quotes.txt') as f:
    one_line = f.readline()
    while one_line:
        if counter % 2 == 0:
            print('   ' + one_line)
        else:
            print(one_line,end='')
        counter += 1
        one_line = f.readline()
print("Done")


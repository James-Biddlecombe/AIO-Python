
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

#Appending to a file
new_name = 'Peña Calderón\n'
with open('Topics\Files\\names.txt','a',encoding='utf-8') as f:
    #f.write(new_name)   <---commented out to avoid too many lines being added
    print("code hashed out to prevent tainting files")
#file closes automatically after indent
print("\nDone")
with open('Topics\Files\\names.txt', 'r',encoding='utf-8') as f:
    print(f.read())
print("Done")

#using tell to determine the pointer location
with open('Topics\Files\\names.txt', encoding='utf-8') as f:
    #read first line to get started
    print(f.tell())
    one_line = f.readline()
    while one_line:
        #the [:-1] is to remove the new line character at the end
        print(one_line[:-1], f.tell())
        one_line = f.readline()
print("Done")

#reading and copying a binary file
"""file_to_copy = 'Topics\Files\happy_pickle.jpg'
name_parts = file_to_copy.split('.')
#create new file with _copy from file to copy
new_file = name_parts[0] + '_copy.' + name_parts[1]
with open(file_to_copy,'rb') as original_file:
    #create or open file to copy to
    with open(new_file,'wb') as copy_to:
        #grab a 4mb chunk to copy at a time
        chunk = original_file.read(4096)
        while len(chunk) > 0:
            copy_to.write(chunk)
            #advance to next chunk
            chunk = original_file.read(4096)
print("File copy complete")
print("Done")"""














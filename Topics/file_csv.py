import csv

#opening a csv file with utf-8, dont read newline characters
with open('Topics\Files\sample.csv',encoding='utf-8',newline='') as f:
    #create a csv row counter and row reader
    reader = enumerate(csv.reader(f))
    #loop through one line at a time, i is counter, row is entire row
    for i, row in reader:
        print(i, row)
print("Done")

#converting strings
with open('Topics\Files\sample.csv',encoding='utf-8',newline='') as f:
    #create a csv row counter and row reader
    reader = enumerate(csv.reader(f))
    #loop through one line at a time, i is counter, row is entire row
    for i, row in reader:
        #row 0 is just columns, ignore it
        if i > 0:
            #whole name split into two at comma
            try:
                full_name = row[0].split(',')
                last_name = full_name[0].strip()
                #first name, strip extra spaces
                first_name = full_name[1].strip()
            except IndexError:
                full_name = last_name = first_name = "<empty>"
            print(first_name, last_name)
print("Done")
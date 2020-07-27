import csv
import datetime as dt


#use these functions to convert any string to appropriate python data type
#get just the first name from full name
def fname(any):
    try:
        nm = any.split(',')
        return nm[1]
    except IndexError:
        return ''

#get just the last name from full name
def lname(any):
    try:
        nm = any.split(',')
        return nm[0]
    except IndexError:
        return ''

#convert string to integer or zero if no value
def integer(any):
    return int(any or 0)

#convert mm/dd/yyyy date to date or none if no valid date
def date(any):
    try:
        return dt.datetime.strptime(any,'%m/%d/%Y').date()
    except ValueError:
        return None

#convert ay string to boolean, false if no value
def boolean(any):
    return bool(any)

#convert string to float, or 0 if no value
def floatnum(any):
    s_balance = (any.replace('$','').replace(',','')).strip()
    return float(s_balance or 0)


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
            #birth year integer, zero for empty string
            birth_year = int(row[1] or 0)
            #date joined is a date
            try:
                date_joined = dt.datetime.strptime(row[2], "%m/%d/%Y").date()
            except ValueError:
                date_joined = None
            #is_active is a boolean, automatically false for empty string
            is_active = bool(row[3])
            #remove $ and , leading and trailing spaces
            str_balance = (row[4].replace('$','').replace(',','')).strip()
            #balance is a float or 0 for empty string
            balance = float(str_balance or 0)
            print(first_name, last_name, birth_year, date_joined, is_active, balance)
print("Done")

#create an empty list of people
people = []
#define a class where each person is an object
class Person:
    def __init__(self, id, first_name, last_name, birth_year, date_joined, is_active, balance):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.date_joined = date_joined
        self.is_active = is_active
        self.balance = balance

#importing csv to python objects
with open('Topics\Files\sample.csv',encoding='utf-8',newline='') as f:
    #create a csv row counter and row reader
    reader = enumerate(csv.reader(f))
    #skip the firstline which is column names
    f.readline()
    #loop through remaining rows one at a time, i is counter, row is entire row
    for i, row in reader:
        #create unique person id and add to people list
        people.append(Person(i, fname(row[0]), lname(row[0]), integer(row[1]), \
                    date(row[2]), boolean(row[3]), floatnum(row[4])))
#when done print the people list
for p in people:
    print(p.id, p.first_name, p.last_name, p.birth_year, p.date_joined, p.is_active, p.balance)
print("Done")

#importing csv to python dictionaries
#create an empty dictionary of people
people = {}
with open('Topics\Files\sample.csv', encoding='utf-8', newline='') as f:
    reader = enumerate(csv.reader(f))
    f.readline()
    for i, row in reader:
        #from each data row in csv file, create a person object with unique id and appropriate data types, add to people list
        newdict = dict({'first_name':fname(row[0]), 'last_name':lname(row[0]), \
                    'birth_year':integer(row[1]), 'date_joined':date(row[2]), \
                    'is_active':boolean(row[3]), 'balance':floatnum(row[4])})
        people[i+1] = newdict
for person in people.keys():
    id=person
    print(id, people[person]['first_name'], \
                people[person]['last_name'], \
                people[person]['birth_year'], \
                people[person]['date_joined'], \
                people[person]['is_active'], \
                people[person]['balance'])
print("Done")





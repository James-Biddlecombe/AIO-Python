import json

#this is the excel data no keys
filename = 'Topics\Files\people_from_csv.json'
#open the file
with open(filename,encoding='utf-8',newline='') as f:
    #load the whole json file into an object named people
    people = json.load(f)
print(people)
print(type(people))
for p in people:
    print(p['Full Name'],p['Birth Year'],p['Date Joined'],p['Is Active'],p['Balance'])
print("Done")
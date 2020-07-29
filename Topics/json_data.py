import json
import datetime as dt

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

#loading unkeyed json from a python string
# Here the JSON data is in a big string named json_string.
# It starts and the first triple quotation marks and extends
# down to the last triple quotation marks.
json_string = """
{
"people": [
{
"Full Name": "Angst, Annie",
"Birth Year": 1982,
"Date Joined": "01/11/2011",
"Is Active": true,
"Balance": 300
},
{
"Full Name": "Schadenfreude, Sandy",
"Birth Year": 2004,
"Date Joined": "03/03/2003",
"Is Active": true,
"Balance": 0
}
]
}
"""
#load json data from the big json_string string
peep_data = json.loads(json_string)
for p in peep_data['people']:
    print(p["Full Name"], p["Birth Year"], p["Date Joined"], p["Is Active"], p["Balance"])
print("Done")

#loading keyed json from a python string
# Here the JSON data is in a big string named json_string,
# It starts and the first triple quotation marks and extends
# down to the last triple quotation marks.
json_string = """
{
"key1": {
"count": 9061,
"lastreferrer": "https://difference-engine.com/Courses/tml-5-1118/",
"lastvisit": "12/20/2018",
"page": "/etg/downloadpdf.html"
},
"key2": {
"count" : 3342,
"lastreferrer" : "https://alansimpson.me/",
"lastvisit" : "12/19/2018",
"page" : "/html_css/index.html"
}
}
"""
#load json data from the big json_string string
hits_data = json.loads(json_string)
for k,v in hits_data.items():
    print(f"{k}. {v['count']:>5} - {v['page']}")
print("Done")

#dumping from string to json
new_dict = json.dumps(hits_data,indent=2,ensure_ascii=False,sort_keys=True)
print(new_dict)
print("Done")

#save or overwrite the existing file
with open('Topics\Files\hitcounts_new.json','w',encoding='utf-8') as out_file:
    json.dump(hits_data, out_file, ensure_ascii=False)
print("Done")
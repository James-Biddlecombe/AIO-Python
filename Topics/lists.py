import math
import random
import datetime as dt
from dateutil.tz import gettz

#creating lists
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
print(students[0])
scores = [88, 92, 78, 90, 84]
print(scores[4])

#looping through a list
scores = [88, 92, 78, 90, 84]
for score in scores:
    print(score)
print("Done")

#seeing if a list contains an item
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
has_anita = "Anita" in students
print("is Anita in the list? ", has_anita)
has_bob = "Bob" in students
print("is Bob in the list? ", has_bob)

#getting the length of a list
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
print(f"There are {len(students)} students in the list.")

#adding an item to the end of the list
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
students.append("Goober")
new_student = "Amanda"
students.append(new_student)
print(students)

#add name only if not in the list already
student_name = "Amanda"
if student_name in students:
    print(student_name, "is already in the list")
else:
    students.append(student_name)
    print(student_name, "was added to the list")

#inserting an item to the list
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
student_name = "Lupe"
students.insert(0,student_name)
print(students)

#changing an item in a list
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
students[3] = "Hobart"
print(students)

#combining lists
list1 = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
list2 = ["Huey", "Dewey", "Louie", "Nader", "Bubba"]
list1.extend(list2)
print(list1)

#removing list items
letters = ["A", "B", "C", "D", "C", "E", "C"]
letters.remove("C")
print(letters)

#removing specific postitions from list
letters = ["A", "B", "C", "D", "E", "F", "G"]
#remove the first item
first_removed = letters.pop(0)
#remove the last item
last_removed = letters.pop()
print(letters)
print(f"the first letter removed was {first_removed} the last was {last_removed}")

#delete a specific item
letters = ["A", "B", "C", "D", "E", "F", "G"]
del letters[2]
print(letters)

#clearing a list
letters = ["A", "B", "C", "D", "E", "F", "G"]
letters.clear()
print(letters)

#count how many times an item appears in a list
grades = ["C", "B", "A", "D", "C", "B", "C"]
b_grades = grades.count("B")
look_for = "C"
c_grades = grades.count(look_for)
print(f"There are {b_grades} B grades in the list")
print(f"There are {c_grades} {look_for} grades in the list")
print("There are " + str(grades.count("F")) + " F grades in the list")

#find a list items index
grades = ["C", "B", "A", "D", "C", "B", "C"]
look_for = "F"
if look_for in grades:
    print(f"{look_for} is at index {grades.index(look_for)}")
else:
    print(f"{look_for} is not in the list")

#alphabetizing and sorting lists
names = ["Zara", "Lupe", "Hong", "Alberto", "Jake", "Tyler"]
numbers = [14,0,56,-4,99,56,11.23]
names.sort()
numbers.sort()
print(names)
print(numbers)

#dates in lists and reverse sort
datelist = []
datelist.append(dt.date(2020,12,31))
datelist.append(dt.date(2019,1,31))
datelist.append(dt.date(2018,2,28))
datelist.append(dt.date(2020,1,1))
datelist.sort(reverse=True)
for date in datelist:
    print(f"{date:%m/%d/%Y}")
print("Done")

#reversing a list
names = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
names.reverse()
print(names)
print("Done")

#copying a list
names = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
backward_names = names.copy()
backward_names.reverse()
print(names)
print(backward_names)
print("Done")
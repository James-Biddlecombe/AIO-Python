import math
import random
import datetime as dt
from dateutil.tz import gettz


#working with if statements
total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
    print(f"Subtotal    : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales tax   : ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total       : ${total:.2f}")

#adding else to the if statement
now = dt.datetime.now()
if now.hour < 12:
    print("Good morning")
else:
    print("Good afternoon")

#handling multiple else's with elif
light_colour = "green"
if light_colour == "green":
    print("Go")
elif light_colour == "red":
    print("Stop")
else:
    print("Proceed with caution")
print("This code executes no matter what")

#repeating a process with a for loop
for x in range(1,10):
    print(x)
print("all done")

#looping through a string
for x in "snorkel":
    print(x)
print("Done")

#looping through a list
for x in ["The", "rain", "in", "Spain"]:
    print(x)
print("Done")
seven_dwarves = ["Happy", "Grumpy", "Sleepy", "Bashful", "Sneezy", "Doc", "Dopey"]
for dwarf in seven_dwarves:
    print(dwarf)
print("And Snow White too")

#exiting a loop
answers = ["A", "B", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is done")

#looping with continue
answers = ["A", "B", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        continue
    print(answer)
print("Loop is done")

#looping with while
counter = 65
while counter < 91:
    print(str(counter) + " - " + chr(int(counter)))
    counter += 1
print("Done")

#starting while loops over with continue
print("Odd numbers")
counter = 0
while counter < 10:
    number = random.randint(1,999)
    if int(number/2) == number/2:
        #even and dont print
        continue
    #otherwise odd and print number incrmenting counter
    print(number)
    counter += 1
print("Done")

#exiting ehile loops with break
print("Numbers that aren't evenly divisible by 5")
counter = 0
while counter < 10:
    number = random.randint(1,999)
    if int(number/5) == number / 5:
        #evenly divisble by 5, bail out
        break
    #otherwise print and keep going
    print(number)
    counter += 1
print("Done")
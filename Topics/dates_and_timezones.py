import math
import random
import datetime as dt
from dateutil.tz import gettz


#working with dates
today = dt.date.today(); print("today: :",today)
last_of_teens = dt.date(2019,12,31); print("last of teens: ", last_of_teens)
print("last of teens month: ", last_of_teens.month)
print("last of teens day: ", last_of_teens.day)
print("last of teens year: ", last_of_teens.year)

#formatting strings for dates
print(f"{last_of_teens:%A, %B %d, %Y}")
todays_date = f"{today:%m%d%Y}"; print("todays date formatted: ", todays_date)

#working with datetime class
midnight = dt.time()
print("midnight: ", midnight)
almost_midnight = dt.time(23,59,59,999999)
print("almost midnight: ", almost_midnight)

#sample date format strings
right_now = dt.datetime.now()
print("datetime right now: ", right_now)

#calculating timespans
new_years_day = dt.date(2019,1,1); print("new years day: ", new_years_day)
memorial_day = dt.date(2019,5,27); print("memorial day: ", memorial_day)
days_between = memorial_day - new_years_day; print("days between: ", days_between)
new_years_day = dt.date(2019,1,1); print("new years day: ", new_years_day)
duration = dt.timedelta(days=146); print("duration timedelta: ", duration)
print("new years plus duration: ", new_years_day + duration)
print("new years minus duration: ", new_years_day - duration)

#birthdate example
now = dt.datetime.now()
birth_datetime = dt.datetime(1985,4,3,8,26); print("brith datetime: ", birth_datetime)
age = now - birth_datetime; print("age: ", age)
print("age datetime type: ", type(age))
today = dt.date.today(); print("today: ", today)
birth_date = dt.date(1985,4,3); print("birth date: ", birth_date)
delta_age = (today - birth_date); print("delta age: ", delta_age)
days_old = delta_age.days; print("days old: ", days_old)
years_old = days_old // 365; print("years old: ", years_old)
months_old = (days_old % 365) // 30; print("months old: ", months_old)
print(f"You are {years_old} years, {months_old} months old, this is {days_old} days old.")

#working with timezones
here_now = dt.datetime.now()
utc_now = dt.datetime.utcnow()
time_difference = (here_now - utc_now)
print(f"my time     : {here_now:%I:%M %p}")
print(f"utc time    : {utc_now:%I:%M %p}")
print(f"Difference  : {time_difference}")
utc = dt.datetime.now(gettz('Etc/UTC'))
print(f"{utc:%A %D %I:%M %p %Z}")
est = dt.datetime.now(gettz('America/New_York'))
print(f"{est:%A %D %I:%M %p %Z}")
cst = dt.datetime.now(gettz('America/Chicago'))
print(f"{cst:%A %D %I:%M %p %Z}")
mst = dt.datetime.now(gettz('America/Boise'))
print(f"{mst:%A %D %I:%M %p %Z}")
pst = dt.datetime.now(gettz('America/Los_Angeles'))
print(f"{pst:%A %D %I:%M %p %Z}")
jhb = dt.datetime.now(gettz('Africa/Johannesburg'))
print(f"{jhb:%A %D %I:%M %p %Z}")
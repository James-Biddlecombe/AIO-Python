import math
import random
import datetime as dt
from dateutil.tz import gettz


#sets are like lists but are not indexed
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
print(sample_set)

#add item to the set
sample_set.add(11.23)
print(sample_set)

#bulk update set
sample_set.update([88, 123.45, 2.98])
print(sample_set)
print("Done")

#copy a set
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
print(sample_set)
ss2 = sample_set.copy()
print(ss2)
print("Done")

#add to set and print neat layout
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
print(sample_set)
print("length of set: ",len(sample_set))
print("is 74.95 in set? ",74.95 in sample_set)
sample_set.add(11.23)
sample_set.update([88,123.45,2.98])
print("\nSample set after .add() and .update()")
print(sample_set)
print("\nLoop through set and print each item formatted.")
for price in sample_set:
    print(f"{price:>6.2f}")

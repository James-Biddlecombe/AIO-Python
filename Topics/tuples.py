import math
import random
import datetime as dt
from dateutil.tz import gettz

#tuples are lists that are immutable and cannot be changed
prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(len(prices))
print(prices.count(4.95))
print(4.95 in prices)

look_for = 12345
if look_for in prices:
    position = prices.index(look_for)
else:
    position = -1
print(position)
for price in prices:
    print(f"${price:.2f}")
print(prices[1])














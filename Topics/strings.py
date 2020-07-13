import math
import random
import datetime as dt
from dateutil.tz import gettz


#This vairable contains an integer
quantity = 14
#This variable contains a float
unit_price = 26.99
#This vairable contains the result of multiplying quantity times unit price
extended_price = quantity * unit_price
#Show the results
print(extended_price)

#abs function
x = -4
y = abs(x)
print("non abs is ", x)
print("as abs is", y)

#round function
x = 1.23456789098765432100000000000000001
y = round(x,2)
print("without round is ", x)
print("with round to 2 places is ", y)

#square root function
num_squareroot = 81
print("The square root of ", num_squareroot, " is ", math.sqrt(num_squareroot))

#f string examples
username = "Alan"
print(f"Hello {username}")
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${unit_price * quantity}")
print(f"Subtotal: ${unit_price * quantity:,.2f}") #2 decimal places fixed

#formatting percent numbers
sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")
print(f"Sales Tax Rate {sales_tax_rate:.2%}")
sample1 = f'Sales Tax Rate {sales_tax_rate:.2%}'
sample2 = f"Sales Tax Rate {sales_tax_rate:.2%}"
sample3 = f"""Sales Tax Rate {sales_tax_rate:.2%}"""
sample4 = f'''Sales Tax Rate {sales_tax_rate:.2%}'''
print(sample1)
print(sample2)
print(sample3)
print(sample4)

#multiline f string example
unit_price = 49.95
quantity = 32
sales_tax_rate= 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f"""
Subtotal:   ${subtotal:,.2f}
Sales Tax:  ${sales_tax:,.2f}
Total:      ${total:,.2f}
"""
print(output)

#formatting width and alignment
output = f"""
Subtotal:   ${subtotal:>9,.2f}
Sales Tax:  ${sales_tax:>9,.2f}
Total:      ${total:>9,.2f}
"""
print(output)

#hex numbers
print("hex of 255 is: ", hex(255))

#complex numbers
z = complex(2,-3)
print("complex(2,-3) is ", z)
print(z.real)
print(z.imag)

#manipulating strings
first_name = "Alan"
middle_init = "C"
last_name = "Simpson"
full_name = first_name + " " + middle_init + ". " + last_name
print(full_name)

#getting the length of a string
s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))

#working with common string operators
s = "Abracadabra Hocus Pocus you're a turtle dove"
print("s = ", s)
print("is there a lowercase letter t in s?", "t" in s)
print("is there an uppercase letter t in s?", "T" in s)
print("print 15 hyphens in a row: ", "-" * 15)
print("print first character in s: ", s[0])
print("print characters 33-39 in s: ", s[33:39])
print("print every 3rd character in s starting at 0: ", s[0:len(s):3])
print("print the lowest char in s(space lower than a): ", min(s))
print("print the highest char in s: ", max(s))
print("where is the first P: ", s.index("P"))
print("where is the first lowercase o in second half of s: ", s.index("o",22,44))
print("how many lowercase a in s: ", s.count("a"))

#manipulating strings with methods
s1 = "There is no such word as schmeedledorp"
s2 = "   a b c   "
s3 = "ABC"
print("capitalise the first letter, rest lower: ", s3.capitalize())
print("count the number of spaces in s1: ", s1.count(" "))
print("find the dot in s3: ", s3.find("."))
print("is s2 all lowercase: ", s2.islower())
print("convert s3 to all lower: ", s3.lower())
print("strip leading characters from s2: ", s2.lstrip())
print("strip leading and trailing from s2: ", s2.strip())
print("swap the case of letters in s1: ", s1.swapcase())
print("show s1 in title case: ", s1.title())
print("show s1 uppercase: ", s1.upper())
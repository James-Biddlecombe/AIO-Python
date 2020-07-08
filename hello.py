import math


#This is a python comment
print("***** basic variable assignment *****")
#This vairable contains an integer
quantity = 14
#This variable contains a float
unit_price = 26.99
#This vairable contains the result of multiplying quantity times unit price
extended_price = quantity * unit_price
#Show the results
print(extended_price)

#abs function
print("***** abs function*****")
x = -4
y = abs(x)
print("non abs is ", x)
print("as abs is", y)

#round function
print("***** round function *****")
x = 1.23456789098765432100000000000000001
y = round(x,2)
print("without round is ", x)
print("with round to 2 places is ", y)

#square root function
print("***** square root function *****")
num_squareroot = 81
print("The square root of ", num_squareroot, " is ", math.sqrt(num_squareroot))

#f string examples
print("***** f string examples *****")
username = "Alan"
print(f"Hello {username}")
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${unit_price * quantity}")


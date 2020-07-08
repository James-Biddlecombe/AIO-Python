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
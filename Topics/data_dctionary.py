import math
import random
import datetime as dt
from dateutil.tz import gettz

#creating a data dictionary
people = {
    'htanaka' : 'Haru Tanaka',
    'ppatel' : 'Priya Patel',
    'bagarcia' : 'Benjamin Alberto Garcia',
    'zmin' : 'Zhang Min',
    'afarooqi' : 'Ayesha Farooqi',
    'hajackson' : 'Hanna Jackson',
    'papatel' : 'Pratyush Aarav Patel',
    'hrjackson' : 'Henry Jackson'
}
print(people)
print(people['zmin'])
person = 'hrjackson'
print(people[person])
howmany = len(people)
print(f"there are {howmany} people in the data dictionary")
print(f"is hrjackson in the dictionary? {'hrjackson' in people}")
print(f"is schmeedleforp in the dictionary? {'schmeedledorp' in people}")
print("Done")

#using get to retrieve data
person = 'bagarcia'
print(people.get(person))

#using get with a error value
print(people.get('schmeedledorp', 'Unbeknownst to this dictionary'))

#changing the value of a key
print(people['hrjackson'])
people['hrjackson'] = "Hanna Jackson-Smith"
print(people['hrjackson'])
print("Done")

#adding and changing dictionary data
people = {
    'papatel' : 'Pratyush Aarav Patel',
    'hrjackson' : 'Henry Jackson'
}
people.update({'hrjackson':'Henrietta Jackson'})
print(people)
people.update({'wwiggins':'Wanda Wiggins'})
print(people)
print("Done")

#print out the dictionary
for person in people.keys():
    print(person + " = " + people[person])
print("Done")

#Looping through a dictionary
people = {
    'htanaka' : 'Haru Tanaka',
    'ppatel' : 'Priya Patel',
    'bagarcia' : 'Benjamin Alberto Garcia',
    'zmin' : 'Zhang Min',
    'afarooqi' : 'Ayesha Farooqi',
    'hajackson' : 'Hanna Jackson',
    'papatel' : 'Pratyush Aarav Patel',
    'hrjackson' : 'Henry Jackson'
}
for person in people:
    print(person)
for person in people:
    print(people[person])
for person in people.values():
    print(person)
for key, value in people.items():
    print(key, " = ", value)
print("Done")

#copying a dictionary
people = {
    'htanaka' : 'Haru Tanaka',
    'zmin' : 'Zhang Min',
    'afrooqi' : 'Ayesha Farooqi'
}
peeps2 = people.copy()
print(people)
print(peeps2)
print("Done")

#delete dictionary items
people = {
    'htanaka' : 'Haru Tanaka',
    'zmin' : 'Zhang Min',
    'afrooqi' : 'Ayesha Farooqi'
}
print(people)
del people["zmin"]
print(people)
print("Done")

#clear a dictionary of items
people = {
    'htanaka' : 'Haru Tanaka',
    'zmin' : 'Zhang Min',
    'afrooqi' : 'Ayesha Farooqi'
}
print(people)
people.clear()
print(people)
print("Done")

#using pop with dictionary
people = {
    'htanaka' : 'Haru Tanaka',
    'zmin' : 'Zhang Min',
    'afrooqi' : 'Ayesha Farooqi'
}
print(people)
adios = people.pop("zmin")
print(adios)
print(people)

#multi-key dictionaries
product = {
    'name' : 'Ray-Ban Wayfarer Sunglasses',
    'unit_price' : 112.99,
    'taxable' : True,
    'in_stock' : 10,
    'models' : ['Black','Tortoise']
}
print(product['name'])
print(product['unit_price'])
print(product['taxable'])
print(product['in_stock'])
print(product['models'])
print("----pretty----")
print('Name:    ',product['name'])
print('Price:   ',f"${product['unit_price']:.2f}")
print('Taxable: ',product['taxable'])
print('In Stock:',product['in_stock'])
print('Models:')
for model in product['models']:
    print(" " * 10 + model)
print("Done")

#fromkeys
#create a generic dictionary for products
product = {
    'name' : '',
    'unit_price' : 0,
    'taxable' : True,
    'in_stock' : 0,
    'models' : []
}
#create a dictionary DWC001 that has the same keys as product
DWC001 = dict.fromkeys(product.keys())
print(DWC001)
print("Done")

#setdefault
#create a generic dictionary for products
product = {
    'name' : '',
    'unit_price' : 0,
    'taxable' : True,
    'in_stock' : 0,
    'models' : []
}
#create a dictionary for product SKU # DWC001
DWC001 = dict.fromkeys(product.keys())
DWC001.setdefault('taxable', True)
DWC001.setdefault('models',[])
DWC001.setdefault('reorder_point',100)
print("Dictionary after fromkeys() and setdefault()")
print(DWC001)
#change the the taxable field from none to True
DWC001['taxable'] = True
print("\nDictionary after fromkeys() and setdefault()")
print(DWC001)
print("Done")

#nesting Dictionaries
products = {
    'RB00111':{'name':'Rayban Sunglasses','price':112.98,'models':['black','tortoise']},
    'DWC0317':{'name':'Drone with Camera','price':72.95,'models':['white','black']},
    'MT50540':{'name':'T-Shirt','price':2.95,'models':['small','medium','large']},
    'ECD2989':{'name':'Echo Dot','price':29.99,'models':[]}
}
print(f"{'ID':<6} {' Name':<17} {'Price':>8}  {' Models'}")
print('-'*60)
#loop through each dictionary int he products dictionary
for oneproduct in products.keys():
    id = oneproduct
    name = products[oneproduct]['name']
    unit_price = '$' + f"{products[oneproduct]['price']:,.2f}"
    models = ''
    #loop through models and tack onto models, 1 item from list then comma and space
    for m in products[oneproduct]['models']:
        models += m + ', '
    #if models length > 2 char then remove last 2 char ', '
    if len(models) > 2:
        models = models[:-2]
    else:
        models = "<none>"
    print(f"{id:<6} {name:<17} {unit_price:>8} {models}")
print("Done")

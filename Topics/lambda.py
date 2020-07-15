#unmasking anonymous functions - lambda
def lowercaseof(s):
    """ Converts string to all lowercase """
    return s.lower()
print(lowercaseof('Zandusky'))
names = ['Adams','Ma','diMeola','Zandusky']
names.sort(key=lowercaseof)
print(names)
print("Done")

#the above as a lambda
names = ['Adams','Ma','diMeola','Zandusky']
names.sort(key = lambda s:s.lower())
print(names)
print("Done")

#more lambda examples
currency = lambda n:f"R{n:,.2f}"
print(currency(12))
percent = lambda n:f"{n:.2%}"
print(percent(.05))
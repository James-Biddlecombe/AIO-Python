def hello(user_name):    #practice function
    """ a docstring describing the function """
    print('Hello ' + user_name)
this_person = 'Alan'
hello(this_person)
print("Done")

#defining optional parameters with defaults
def hello_1(user_name = 'nobody'):
    """ a docstring describing the function """
    print('Hello ' + user_name)
hello_1('Alan')
hello_1()
print("Done")

#passing multiple values to a function
def hello_2(fname, lname, datestring):
    """ a docstring describing the function """
    print('Hello ' + fname + ' ' + lname)
    print('The date is ' + datestring)
hello_2('Alan', 'Simpson', '12/31/2019')
print("Done")

#using default blank values in function
def hello_3(fname, lname, datestring=''):
    """ a docstring describing the function """
    msg = 'Hello ' + fname + ' ' + lname
    if len(datestring) > 0:
        msg += ' you mentioned ' + datestring
    print(msg)
hello_3('Alan','Simpson','12/31/2019')
hello_3('Alan','Simpson')
print("Done")

#using keyword arguments (kwargs)
def hello_4(fname, lname='<Unknown>', datestring=''):
    """ a docstring describing the function """
    msg = 'Hello ' + fname + ' ' + lname
    if len(datestring) > 0:
        msg += ' you mentioned ' + datestring
    print(msg)
hello_4(fname='James',datestring='03/04/1985')
appt_date = '12/03/2019'
last_name = 'Janda'
first_name = 'Kylie'
hello_4(fname=first_name,lname=last_name,datestring=appt_date)
print("Done")

#passing multiple values in a list
def alphabetize(original_list=[]):
    """ pass any list in [], displays a string with them sorted """
    sorted_list = original_list.copy()
    sorted_list.sort()
    final_list = ''
    for name in sorted_list:
        final_list += name + ", "
    if len(final_list) > 2:
        final_list = final_list[:-2]
    else:
        final_list = "An empy list was passsed"
    print(final_list)
names = ['bob','charlie','dale','alice']
alphabetize(names)
print("Done")

#passing an arbitary number of arguments
def sorter(*args):
    """ pass any number of args seperated by commas
    inside the function they are treated as a tuple named args """
    newlist = list(args)
    newlist.sort()
    print(newlist)
sorter(1,0.001,100000,-900,2)
print("Done")

#returning values from functions
def alphabetize_1(original_list=[]):
    """ pass any list in [], displays a string with them sorted """
    sorted_list = original_list.copy()
    sorted_list.sort()
    final_list = ''
    for name in sorted_list:
        final_list += name + ", "
    if len(final_list) > 2:
        final_list = final_list[:-2]
    else:
        final_list = "An empy list was passsed"
    return final_list
random_list = ['McMullen','Keaser','Maier','Wilson','Yudt','Gallagher','Jacobs']
alpha_list = alphabetize_1(random_list)
print(alpha_list)
print("Done")

#show number in currency format, specify width
def currency(n, w=15):
    """ show in currency format, width default 15 or specified """
    s = f"${n:,.2f}"
    return s.rjust(w)
print(currency(9999))
print(currency(9999,20))
print("Done")

#show number in percent format, specify width
def percent(n, w=15):
    """ show in percent format width default to 15 or specify """
    s = f"{n:.1%}"
    return s.rjust(w)
print(percent(.15))
print(percent(.15,20))
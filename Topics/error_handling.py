


class Error(Exception):
    """ Base class for other exceptions """
    pass

class EmptyFileError(Error):
    """ Inherited class from Error, for empty files """
    pass


try:
    #open the file and show its contents
    thefile = open('Topics\Files\people.csv')
    #count the number of lines in file
    line_count = len(thefile.readlines())
    #if there are fewer than 2 lines raise exception
    if line_count < 2:
        raise EmptyFileError
except FileNotFoundError:
    #the above exception handles error 2 File Not Found
    print("Sorry, I don't see a file anmed people.csv here")
except EmptyFileError:
    print('\nYour people.csv file does not have enough data.')
    thefile.close()
except Exception as err:
    #the above handles all other exceptions not specified
    print(err)
    thefile.close()
else:
    print()
    for one_line in thefile:
        print(one_line)
    thefile.close()
    print("Success!")
finally:
    #this executes always
    print("FINALLY")
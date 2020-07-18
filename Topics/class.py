import datetime as dt


#creating a class
class Member:
    #Member variable
    free_days = 365
    expiry_days = 365

    #Member Object
    """ create a member from uname and fname """
    def __init__(self, username, fullname):
        #Member object attribute
        self.username = username
        self.fullname = fullname
        self.datejoined =dt.datetime.today()
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)
        self.isactive = True
        self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)
    #Member methods
    def show_datejoined(self):
        """ method to show the datejoined """
        return f"{self.fullname} joined on {self.datejoined:%m/%d/%y}"
    def activate(self, yesno):
        """ method to set member to active or inactive passing True or False """
        self.isactive = yesno
    def showexpiry(self):
        """ method to sow the expiry """
        return f"User {self.username} with name {self.fullname} expires on {self.expiry_date}"
    def get_status(self):
        return f"{self.fullname} is a Member"
    #Class methods
    @classmethod
    def setfreedays(cls,days):
        cls.free_days = days
    #Static method
    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%I:%M %p}"

#creating a subclass for admins
class Admin(Member):
    #Admin accounts dont expire for 100 years
    expiry_days = 365.2422 * 100
    #create object same as base with extra var: secret_code
    def __init__(self, username, fullname, secret_code):
        #pass the member params back up to base class member
        super().__init__(username, fullname)
        #assign the remaining params for this object
        self.secret_code = secret_code
    #same name definition overrides ase class definition
    def get_status(self):
        return f"{self.fullname} is an Admin"

#creating a subclass for users
class User(Member):
    #same name definition overrides base class definition
    def get_status(self):
        return f"{self.fullname} is a regular User"


newguy = Member('Rambo','Rocco Moe')
print(newguy)
print(newguy.username)
print(newguy.fullname)
print(type(newguy))
print("Done")
newguy.username = "Princess"
print(newguy.username)
print(newguy.fullname)
print("Done")
print(newguy.show_datejoined())
print(newguy.isactive)
newguy.activate(False)
print(newguy.isactive)
print("Done")
wilbur = Member('wblomgren','Wilbur Blomgren')
print(wilbur.datejoined)
print(wilbur.free_expires)
print(wilbur.free_days)
print("Done")
Member.setfreedays(30)
wilbur2 = Member('wobbly2','Wilbur Number 2')
print(wilbur2.free_days)
print(wilbur2.currenttime())
Member.setfreedays(365)
print("Done")

#subclass work
Ann = Admin('Annie','Angst','PRESTO')
print(Ann.username)
print(Ann.fullname)
print(Ann.secret_code)
print(Ann.expiry_days)
print(Ann.get_status())
print()
Uli = User('Uli','Ungula')
print(Uli.username)
print(Uli.fullname)  
print(Uli.expiry_days)
print(Uli.showexpiry())
print(Uli.get_status())
Manny = Member('Mindy','Membo')
print(Manny.get_status())
print("Done")

#help(Admin)
#print(Admin.__dict__)
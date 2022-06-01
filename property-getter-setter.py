"""
@property decorator
"""
class Employee:

    def __init__(self, f_name, l_name) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.email = f_name + l_name + '@gmail.com'

    # instance method
    def full_name(self):
        return self.f_name + ' ' + self.l_name

# now in case we need to add more opertations on email vaiale then we can user property decorator

class Employee:

    def __init__(self, f_name, l_name) -> None:
        self.f_name = f_name
        self.l_name = l_name
        # self.email = f_name + l_name + '@gmail.com'

    # instance method
    def full_name(self):
        return self.f_name + ' ' + self.l_name

    @property
    def email(self, extension):
        return self.f_name + self.l_name + '@' + extension

    # this will not break above variable of email and can be used a variable

emp = Employee("Deep", "Patel")
emp.email 

# property method allows us to create method that we can access like an attribute
# Conclusion - Define like method and access like variable

"""
getter, setter and deleter
"""
# What if we want to do reverse of full_name method, which can set f_name and l_name?
# Like: emp.full_name = "Deep Velani" 
# Which makes emp.f_name to "Deep" and emp.l_name to "Velani"
# To do that we need to make full_name a property
class Employee:

    def __init__(self, f_name, l_name) -> None:
        self.f_name = f_name
        self.l_name = l_name
        # self.email = f_name + l_name + '@gmail.com'

    @property    # chaned from instance method to property method
    def full_name(self):
        return self.f_name + ' ' + self.l_name

    # to set full name
    @full_name.setter
    def full_name(self, name):
        f_name, l_name = name.split(' ')
        self.f_name = f_name
        self.l_name = l_name

    # to delete full_name
    @full_name.deleter
    def full_name(self):
        self.f_name = None
        self.l_name = None
        print("Deleted!")

    @property
    def email(self, extension):
        return self.f_name + self.l_name + '@' + extension


emp = Employee("Deep", "Patel")
# setter 
emp.full_name = "Meet Velani"
# deleter 
del emp.full_name

# @property is getter and can be intialised simply like shown below

class Geeks:
     def __init__(self):
          self._age = 0
       
     # function to get value of _age
     def get_age(self):
         print("getter method called")
         return self._age
       
     # function to set value of _age
     def set_age(self, a):
         print("setter method called")
         self._age = a
  
     # function to delete _age attribute
     def del_age(self):
         del self._age
     
     age = property(get_age, set_age, del_age) 
  
# OBJECT INTROSPECTION
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname ==None:
            return "Email is not set. Please set is using setter."
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting Now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = (Employee("Skill", "F"))
print(type(skillf))  # This is a way of object introspection.
print(type("This is string"))  # This comes from the string class.
print(id("This is a string"))
o = "This is a string"
print(id("That That"))
print(dir(o))  # This gives the functions which we can use with it.
print(dir(skillf))
import inspect
print(inspect.getmembers(skillf))  # This gives all the attributes.
            # Google for more inspect module functions.

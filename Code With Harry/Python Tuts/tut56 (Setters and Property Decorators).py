# SETTERS AND PROPERTY DECORATORS
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property  # This makes the email run as a string.
    def email(self):
        if self.fname==None or self.lname ==None:  # To prevent the email to be printed as None.None@codewithharry.com.
            return "Email is not set. Please set is using setter."
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting Now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]  # This can be combined and run.
        self.lname = names.split(".")[1]

    @email.deleter  # This is made to delete the object.
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter =  Employee("Hindustani", "Supporter")
nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.explain())  # This prints the object.
print(hindustani_supporter.email)

hindustani_supporter.fname = "US"
print(hindustani_supporter.email)  # This will remain same as when the object was created that time the email was created.
# After making another function the email changes.
hindustani_supporter.email = "This.that@codewithharry.com"  # This runs as the setter function is there to handle it.
print(hindustani_supporter.fname)
print(hindustani_supporter.lname)  # The properties of the object got changed.
print(hindustani_supporter.email)

del hindustani_supporter.email  # This doesnt find the deleter therefore it shows error. Therefore the deleter is created.
print(hindustani_supporter.email)  # This shows None.None@codewithharry.cam as the fname and lname are None.
hindustani_supporter.email = "Harry.Perry@codewithharry.com"  # The email is again set using this.
print(hindustani_supporter.email)

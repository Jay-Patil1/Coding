# STATIC METHODS
# To program without self or cls.
# Static methods are made through a decorator staticmethod.
# Just to keep it in the class.

class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetails(self):
        return(f"Name is {self.name}, Salayr is {self.salary} and Role is {self.role}")

    @classmethod # Decorator
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod # This is put in the class to just use for the objects.
    def printgood(string):
        print("This is good " + string)


harry = Employee("Harry",355, "Instructor")
rohan = Employee("Rohan",555, "Student")
karan = Employee.from_dash("Karan-480-Student")

print(karan.salary)
print(karan.no_of_leaves)
print(karan.printgood("Harry"))  # There is nothing to return therefore it prints none.
# Static Method and Class Methods are used for efficient and pricise program.
Employee.printgood("Karan")
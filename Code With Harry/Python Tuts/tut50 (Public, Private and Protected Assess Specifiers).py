# PUBLIC, PRIVATE AND PROTECTED ACCESS SPECIFIERS
# Public - Anyone can use.
# Protected - Only the home ones.
# Private - Only for the a specific one.


class Employee:
    no_of_leaves = 8  # This is a public variable.
    var = 8
    _protected = 9  # This is a protected variable. This variable can be used by the base class and the derived class. And not the other class.
    __private = 98  # This is private variable. This cannot be used in other classes.

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return(f"Name is {self.name}, Salayr is {self.salary} and Role is {self.role}")

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


emp = Employee("Harry", 345, "Programmer")
print(emp._protected)  # This can be printed.
# print(emp.__private) # We cant access this like this.
                # Name Angling
print(emp._Employee__private) # We can access the private variable using name angling.
# This prevent the use of this variable outside.

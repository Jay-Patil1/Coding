# OPERATOR OVERLOADING AND DUNDER METHODS


class Employee:
    no_of_leaves = 8


    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetails(self):
        return(f"Name is {self.name}, Salayr is {self.salary} and Role is {self.role}")

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other): # This is special method (Dunder add) used for operator overloading.
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return (f"Name is {self.name}, Salayr is {self.salary} and Role is {self.role}")
        return f"Employee({self.name}, {self.salary}, {self.role})" # Generally used like this.

    def __str__(self):
        return f"Employee({self.name}, {self.salary}, {self.role})"


emp1 = Employee("Harry", 445, "Programmer")
emp2 = Employee("Rohan", 8, "Cleaner")
print(emp1 + emp2)
print(emp1 / emp2)
print(str(emp1))  # If str isnt available theen the repr is used.

        # Mapping operators to Functions (Google)

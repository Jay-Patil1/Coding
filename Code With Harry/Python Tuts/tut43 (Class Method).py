# CLASS METHODS
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetails(self):
        return(f"Name is {self.name}, Salayr is {self.salary} and Role is {self.role}")

    @classmethod # Decorator
    def change_leaves(cls, newleaves):# cls is the class whose instance is the object. This is used to change the class variable.
        cls.no_of_leaves = newleaves



harry = Employee("Harry",355, "Instructor")
rohan = Employee("Rohan",555, "Student")

Employee.no_of_leaves = 89
print(harry.salary)
print(harry.no_of_leaves) # This forst finds for instance variables but if it isnt available it goes to class variable.
harry.change_leaves(34)
print(harry.no_of_leaves) # This can change the value of the class variable.
print(Employee.no_of_leaves)
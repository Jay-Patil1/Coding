# SINGLE INHERITANCE
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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class Programmer(Employee): # () This inherits the properties of the class.
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, language):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = language
# This is one way to this.The is other is super.
    def printprog(self):
        return f"The Programmer's name is {self.name}, Salary is {self.salary}, and role is {self.role} The languages are {self.languages}"


harry = Employee("Harry",355, "Instructor")
rohan = Employee("Rohan",555, "Student")
karan =Programmer("Karan",777,"Programmer", ["Python","C++"])
shubham = Programmer("Shubham",555,"Programmer",["Python", "C++"])
print(karan.printprog())

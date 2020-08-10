# CLASS METHODS AS ALTERNATIVE CONSTRUCTORS
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
        params = string.split("-") # Splits the string from - and makes a list out if it.
        print(params) # This prints the split string.
        return cls(params[0], params[1], params[2])

        # return cls(*string.split("-")) # This os the one liner for the above code.


harry = Employee("Harry",355, "Instructor")
rohan = Employee("Rohan",555, "Student")
karan = Employee.from_dash("Karan-480-Student")

print(karan.salary)
print(karan.no_of_leaves)
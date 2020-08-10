# SELF AND __INIT__() (CONSTRUCTORS)
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole): # This is a constructor. Which takes arguements.
        self.name = aname
        self.salary = asalary
        self.role = arole

    # We will create a function in the class.
    def printdetails(self): # Self is the object worked upon.
        return(f"Name is {self.name}, Salayr is {self.salary} and Role is {self.role}")

harry = Employee("Harry",355, "Instructor")
rohan = Employee("Rohan",555, "Student")

harry.name = "Harry"
harry.salary = 445
harry.role = "Instruntor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(rohan.printdetails()) # This makes the 'rohan' go into the function.
print(harry.printdetails())

                    # Constructors
harry = Employee("Harry",355, "Instructor") # This goes to init. If theres no init it doesnt work . As the class doesn't take arguements.
print(harry.salary)
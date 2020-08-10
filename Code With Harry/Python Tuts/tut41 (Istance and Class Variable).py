# INSTANCE AND CLASS VARIABLES
class Employee:
    no_of_leaves = 8 # Class name should start form capital for convention.
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 445
harry.role = "Instruntor"

rohan.name = "Rohan"
rohan.salary = 4554  # These are the own properties of the objects.
rohan.role = ("Student")
print(rohan.name)
print(harry.salary)
print(harry.no_of_leaves) # This is same for all objects as it is a template.
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
print(Employee.__dict__) # This is the dictionary of the object.
Employee.no_of_leaves = 9 # This changes the properties of all the objects. The class variable cannot be changed using an object.
rohan.no_of_leaves = 10 # This changes the properties of the specific object.
print(rohan.no_of_leaves)
print(Employee.__dict__) # The dictionary of the object is changed.
 # All the objects share the clas variable.

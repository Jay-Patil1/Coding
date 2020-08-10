# CREATING OUR FIRST CLASS
class Student:
    pass # This means make it empty.
harry = Student() # Instance. # OBJECT.
larry = Student()  # Instancce # OBJECT.

harry.name = "Harry" # Instance vaariable.
harry.std  = 12
harry.section = 1
larry.std = 9
larry.subjects = ["Hindi", "Pysics"]
print(harry.section ,",",larry.std) # Prints the instance variables. Harry and Larry are two different.

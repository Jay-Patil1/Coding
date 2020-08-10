# USING EXTERNAL AND BUILD IN MODULES
import random
# Random is a module and is imported into the project.
# We can access sub-modules and the functions.
# For knowing functions of a module we can google it.
random_number = random.randint(0,5) # Gives any Number form 0 to 5.
print(random_number)# Can be used to
rand = random.random()*100 # This helps access the submodule.
print(rand)
lst = ["Star Plus","DD1","Aaj Tak","Code With Harry"] # Prints a randon value of the list.
choice = random.choice(lst)
print(choice)
# External modules are installed using pip.
# Make a program with any 2 modules and 2 functions of them.

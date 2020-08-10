# HOW IMPORT WORKS
import sklearn as sk
print(sk.__version__) # Gives the versin the the module.
import sys # This is assigned to the current global scope.
print(sys.path)

import File1
from File1 import a
print(a)# Direct access to the variable.
print(File1.a) # # This helps while using (importing) many files.
File1.printjoke(" This is me.") # Functions from the file can be used.
# If file name matches the name of a module or package then we cannot use the module or package.
# int, float in built variables.
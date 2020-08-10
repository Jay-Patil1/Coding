# FUNCTIONS AND DOCSTRINGS
a = 9
b = 8
c = sum((a,b)) # Build in Function
print(c)

# Making user defined Functions
def function1(a,b): # Used to define a function.This function is without input.
    print("Hello you are in function 1",a+b)

function1(5,7)#() Its a rule.It should be added.
# Function can be printed for many times.
# Just the function name also funs the function.
def function2(a, b): # This is an input function.
    """This function only works for 2 numbers."""
    average = (a+b)/2
    # print(average)
    return average # Used if the function is used as variable.

v = function2(5, 7) # Gives the function the value of a and b.
print(v)
# First functions should be defined then should be used.
# Functions make it easy for not to type the function always.
# Functions have docstrings.
# Docstring is a string written it the function as the first line.
print(function2.__doc__) # This prints the docstring of the function.
# Docstring should be used so as to help the other programmer get to know about the function.
# Functions are easy to edit and use.

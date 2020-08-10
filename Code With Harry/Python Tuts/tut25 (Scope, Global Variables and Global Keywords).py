 #  SCOPE, GLOBAL VARIABLES AND GLOBAL KEYWORDS
l = 10
a = 5# Global Variable. Any function in this program can use this.This is in global scope.
def function1 (n):
    l = 5 # Local Variable of the function.This is local scope.This is only applicable for the function.
    m = 8 # If Local variable is not found it goes for Global variable.
    a = a+45 # Global variables cannot be edited by a function.In a function
    print(l,m)
    print(n,"I have printed")

function1("This is me")
print(l)
print(m)# Local variables cannot be printed outside.

                        # Global Keyword
def function2(n):
    global l # This gives the function the permission to cgange a global variable.
    l = l+45
    print(l,)

function2("This is me")
x = 89
def Jay():
    x = 20
    def Rohan(): # This is Nested function. Function in afunction.
        global x # Global variable goes out of the function.Not out of the nested function.If variable isn't availabe it is created.
        x = 88
    print("before calling rohan()",x)
    Rohan()
    print("after calling rohan()",x)

Jay()
print(x) # This goes out of the function and makes a global variable x.


                        #QUIZ
# What will print(x) print?
# Ans - 88 as according to function Rohan it changed the variable to 88.


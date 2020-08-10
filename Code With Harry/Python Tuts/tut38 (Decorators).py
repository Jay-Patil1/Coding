# DECORATORS
# def function1():
#     print("subscribe Now")
#
# func2 = function1
# del function1
# func2() # After deleting function 1 it get run as it is = to function1

# def function(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=function(1)
# print(a)
# We can return a function using other function.
# def executor(func):
#     func("this")
# executor(print) # We can return functions using other functions.


def dec1(func1):
    def nowExec(): # Sub function.
        print("Executing now")
        func1()
        print("Executed")
    return nowExec

@dec1 # This makes the function a decorator.
def who_is_jay():
    print("Jay is a good boy.")

# who_is_jay = dec1(who_is_jay) # This another way of using a decorator.
# who_is_jay is run throung dec1 (Decorator).
who_is_jay()
# This is used for using multiple functions with the same func tion.

# ANONYMOUS/LAMBDA FUNCTIONS
# Lambda functions are just for convenience.
# Lambda functions and Anonymous functions.
# def add(a,b):
#     return a+b
#
# minus = lambda x,y: x-y
# # The upper lambda is a short form of the following function.
# def minus(x,y):
#     return x-y
# print(minus(9,4))
def a_first(a):
    return a[1] # First index of a.
a = [[1,14],[5,6],[8,23]]
a.sort(key=a_first)
print(a)
        # Lambda for the upper function.

a = [[1,14],[5,6],[8,23]]
a.sort(key=lambda x:x[1]) # Makes a function which takes input and gives its first index.
print(a)
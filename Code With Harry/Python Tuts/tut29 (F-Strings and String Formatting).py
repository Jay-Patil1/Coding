# F-STRINGS AND STRING FORMATTING
import math
me = "Harry"
a = "This is %s"%me # This is a way of string formatting.
print(a)
a1 = 3
# a = "This is %s %s"%(me,a1)# This is another way of string formatting.
a = "This is {} {}"
b = a.format(me,a1) # .format is another way of formatting a string.
print(b)
a = f"This is {me} {a1} {4*65} {math.cos(65)}"# We can use anything into a f string.
print(a)

# MAP, FILTER AND REDUCE
                        # Map Function
# This applies a function to the whole list.

numbers = ["3", "34", "64"]

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
# Map function can be used as an alternative for for loop.
numbers = list(map(int, numbers))# (what to apply, where to apply ).This goes into the list and modifies it.
print(map(int, numbers))

numbers[2] = numbers[2] + 1
print(numbers[2])
def sq(a):
    return a*a
num = [2,3,5,6,76,3,3,2]
square = list(map(sq, num))
print(square)
num = [2,3,5,6,76,3,3,2]
square = list(map(lambda x: x*x , num)) # Map and lambda can be used together.
print(square)

def square(a):
    return a*a

def cube(a):
    return a*a*a
func = [square, cube]
for i in range(5):
    val = list(map(lambda x:x(i), func)) # If lambda is given a function then it gives function(i)
    print(val)


                        # Filter Function
list1 = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9]
def is_grater_5(num):
    return num > 5

gr_than_5 = list(filter(is_grater_5, list1)) # Helps only get the True values.
print(gr_than_5)

                            # Reduce
from functools import reduce

list1 = [1,2,3,4]
num = 0
for i in list1:
    num = num + i
print(num)
# Reduce is used as and alternative for this.
num = reduce(lambda x,y:x+y,list1) # (function, where to apply)
print(num)
# Map Filter Reduce just help us get the code reduced.

# GENERATORS 
# Generators can be iterated only once.
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""


def gen(n):
    for i in range(n):
        yield i  # This generators values on the fly.


g = gen(3)  # This value doesn't get stored. It is generated for all the times.
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())  # This gives an error as the generator is not capable to generate beyond 3.
for i in g:
    print(i)

# Make Generator for-
# Fibonachi Series.
# Factorial.
h = "Jay"  # A string is iterable.#
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

for c in h:
    print(c)  # The string is iterated.
# An integer is not iterable.

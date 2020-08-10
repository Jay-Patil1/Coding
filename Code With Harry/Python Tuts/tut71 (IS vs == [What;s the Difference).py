# 'IS' VS '==': WHAT'S THE DIFFERENCE?
# == - Value Equality. - Two objects have the same value.
# is - Reference Equality. - Two references refer to the same object.
a = [5, 4, 1]
b = a
print(b == a)
print(b is a)
c = a[:]
print(c == a)
print(c == b)
print(c is a)
print(c is b)

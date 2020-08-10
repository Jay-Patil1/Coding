# DIAMOND SHAPE PROBLEM IN MULTIPLE INHERITANCE
# Which class uses which method is a diamond problem.
# Java doesn't allow multiple inheritance.
# B and C are made from A.
# And D is made form B and C.

class A:
     def met(self):
         print("This is amothod from class A.")


class B(A):
    def met(self):
        print("This is amothod from class B.")


class C(A):
    def met(self):
        print("This is amothod from class C.")

class D(C, B):
    def met(self):
        print("This is amothod from class D.")


a = A()
b = B()
c = C()
d = D()

d.met()  # The met() is searched for the method in:
# 1] D
# 2] C
# 3] B
# 4] A

# SUPER() AND OVERRIDING


class A:
    classvar1 = "I am a class variable in class A."

    def __init__(self):
        self.var1 = "I am inside class A's constructor."
        self.classvar1 = "Instance variable in class A."
        self.special = "Special"


class B(A):
    classvar1 = "I am in class B."

    def __init__(self):   # The upper constructor is overrided.
        super().__init__()  # This runs the constructor of the super class.
        self.var1 = "I am inside class B's constructor."
        self.classvar1 = "Instance variable in class B."
        print(super().classvar1)  # This can be used to access the variables of the superclas.


a = A()
b = B()
print(b.special, b.var1, b.classvar1)  # It first goes for the instace variable.
# First goes for instance variable in B.
# Then goes to A.
# Then goes for class variable in B.
# Then goes to class variable in A.

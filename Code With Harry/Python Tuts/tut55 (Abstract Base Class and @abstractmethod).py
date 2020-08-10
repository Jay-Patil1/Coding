# ABSTRACT BASE CLASS AND @ABSTRACTMETHOD
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod


class Shape(ABC):  # This is a abstract base class.
    @abstractmethod  # This method is forced to be implimented into the class
    def printarea(self):
        return 0

# class Shape(metaclass=ABCMeta): # This is also used instead of the upper.
#     @abstractmethod # This method is forced to be implimented into the class
#     def printarea(self):
#         return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.printarea())
tryobj = Shape() # Objects cant be made using abstract base class.

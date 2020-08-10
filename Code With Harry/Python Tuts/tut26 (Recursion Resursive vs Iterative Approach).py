# RECURSION:RECURSIVE VS ITERATIVE APPROACH
# Recursion means using a function in a function.
# def print2(str1):
#     print2(str1)
#     print("This is "+str1)
#
# print2("JAY")
# Factorial works like this
# n! = n * n-1 * n-2 * n-3........1
# n! = n*(n-1)!
def factorial_iterative(n):
    """
      :param n: Integer
      :return: n * n-1 * n-2 * n-3........1
      """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac


number = int(input("Enter the number"))
print("Factorial using iterative method",factorial_iterative(number))

                # Recursive Method
def factorial_recursive(n):
    """

      :param n: Integer
      :return: n * n-1 * n-2 * n-3........1
      """
    if n ==1 :
        return 1
    else:
        return n * factorial_recursive(n-1)

print("Factorial using recursive method",factorial_recursive(number))
#  Recursive works like
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1 = 120



                    # QUIZ
# Fibonacci Sequence
# 0,1,1,2,3,5,8,
# Function for calculating Fibonacci Sequence
def fibonacci(n):
    if n == 1:
        return 0
    elif n ==2 :
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number = int(input("Enter a Number"))
print(fibonacci(number))

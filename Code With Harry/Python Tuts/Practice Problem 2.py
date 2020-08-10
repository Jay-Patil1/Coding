# DIVIDE THE APPLES
# Harry Potter has got n number of apples.
# Harry has some students among whom he wants to distribute the apples equally.
# These n numbers of apples are provided to Harry by his friends and he can request for few more or few less apples.
# You need to whether a number in mn to mx is a divisor or not.
# If mn = mx Show this is not a range. Show the result also.
# Input:
    # Take imput n, mn and mx from the user.
# Output:
    # Print whether the numbers between mn amd mx are divisor or not.
# Example:
    # n=2, mn=2 and mx=5
    # 2 is a divisor if 20
    # 3 is not a divisor of 20
    # 5 is divisor of 20

                    # SOLUTION

'''
Author: Jay Patil
Date: 7 August 2020
Purpose: Practice Problem
'''

apples = int(input("Enter the number of apples:\n"))
mn = int(input("Enter the minimum number to check:\n"))
mx = int(input("Enter the maximum number to chech:\n"))

for i in range(mx, mn+1):
    if apples%i == 0:
        print(f"{i} is a divisor of {apples}")

    else:
        print(f"{i} is not a divisor of {apples}")

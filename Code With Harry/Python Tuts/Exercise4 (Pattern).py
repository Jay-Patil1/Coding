# EXERCISE 4
# # Pattern Printing.
# input = integer n
# Boolean = True or False
# Tue
# *
# **
# ***
# ****
# False
# ****
# ***
# **
# *
# n = No. of rows.
                        # SOLUTION

'''
Author: Jay Patil
Purpose: Learning Python
'''

print("Peattern Printing")
num1 = int(input("Enter how many rows you want : "))
print("Enter 0 or 1")
bool_val = input("1 for true value and 0 for false :")
if bool_val == "1":
        for i in range(0,num1+1):
            print("*"*i)
if bool_val == "0":
        for i in range(num1,0-1):
            print("*"*i)
            
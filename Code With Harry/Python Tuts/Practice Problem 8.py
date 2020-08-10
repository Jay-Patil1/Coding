# ROHAN DAS IS A FRAUD
# Rohan Das is a fraud by nature.
# Rohan Das wrote a python function to print a multiplication table of a given number.
# He put one of the values (randomly generated) as wrong.
# Rohan Das did this to fool his classmates and make them commit a mistake in a Test.
# You decide to use your python skill to counter his actions.
# Write a programm to validate Rohan's table.
# You should find out the wrong value in Rohan's table  and expose Rohan Das as a fraud.
# Note : Rohans function returns a list of numbers like:
    # [6, 12, 18, 26,...,60]
# You return the index where Rohan's Table is wrong.
# If table correct return None.

                    # SOLUTION  

'''
Author: Jay Patil
Date: 9 August 2020
Purpose: Practice Problem
'''

import random

def rohanMultiplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1,11)]
    table[wrong] = table[wrong] + random.randint(0,4)
    return table

def isCorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i - 1
    return None

if __name__ == "__main__":
    # print(rohanMultiplication(7))
    number = int(input("Enter a number:\n"))
    myTable = rohanMultiplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"Table is wrong at : {wrongIndex + 1}")

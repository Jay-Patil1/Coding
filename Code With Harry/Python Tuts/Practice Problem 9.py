# FUNNY NAMES
# Its result day at school and everyone's not happy.
# You make your friends laugh by jumbling thier names.
# Take input of number of names.
# Give the funny names as output.

# Input:
    # Enter the number of Friends:
    # 2
    # Enter the name of Friends:
    # Jay Patil
    # Swayam Shah

# Output:
    # Jay Shah
    # Swayam Patil

                    # SOLUTION

'''
Author: Jay Patil
Date: 9 August 2020
Purpose: Practice Problem
'''

'''Generate a random number.
   Swap the names using the random number.
   Split the names.'''

import random

names = int(input("Enter the number of friends:\n"))
allnames = []
fnames = []
lnames = []
for i in range(names):
    name = input("Enter the name:\n")
    allnames.append(name)
    fnames.append(name.split(" ")[0])
    lnames.append(name.split(" ")[1])

print(f"The names are:\n{fnames}")
print(f"The last names are:\n{lnames}")

rlnames = []

while True:
    rlname = random.randint(0, len(lnames)-1)
    rlnames.append(rlname)
    if len(rlnames) == len(lnames):
        break


print("The jumbled names are:")
for i in range(0,len(lnames)):
    rlname1 = random.randint(0, len(rlnames)-1)
    print(f"{fnames[i]} {lnames[rlname1]}")

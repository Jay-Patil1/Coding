# YOUR AGE IN 2090
# Take input from the user. (age or birth year)
# Tell them when will they turn 100 yrs old.
# No modules like datetime or dateutils.
# Can optionally provide a year and tell their age in that year.
# Handle all errors like :
    # Not yet born
    # Seem to be the oldest person alive.
    # And any other errors if possible.

                    # SOLUTION

'''
Author: Jay Patil
Date: 7 August 2020
Purpose: Practice Problem
'''

yearAge = int(input("What is your Age/Year of Birth:\n"))

isAge = False
isYear = False


if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if yearAge<1900 and isYear:
    print("You semm to be the oldest person alive!")
    exit()

if yearAge>2020:
    print("You are not yet born!")
    exit()

if isAge:
    yearAge = 2020 - yearAge

print(f"You will be 100 years old in {yearAge + 100}")  

interestedYear = int(input("Enter the year you want to know your age in:\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")

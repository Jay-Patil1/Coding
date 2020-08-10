# FOODS AND CALORIES
# You visit a restaurant called Code With Harry.
# Food items in this restaurant are sorted based on thier calories content.
# Reverse this list of food items and their calories.
# Use following 3 methos to reverse a lise:
# Inbuilt method
# listname[::-1] Slicing
# Swapping first element with last second with second last and so on.

# Input:
    # Take a list as an input from the user.

# Output:
    # Reverse the list.
    # Print all the 3 lists using the 3 methods.
    # Check if all methods print same list.

                    # SOLUTION

'''
Author: Jay Patil
Date: 7 August 2020
Purpose: Practice Problem
'''

# Take the size of list from the user.
print("Enter the number of the list one by one:\n")
size = int(input("Enter the size of the list:\n"))

mylist = []  # Initialize a blank list.

# Take the input from the user one by one.
for i in range(size):
    mylist.append(int(input("Enter list element:\n")))

print(f"Your list is {mylist}\n")

# Method 1
reverse1 = mylist[:]  # Saves reverse as the copy of mylist.
reverse1.reverse()
print(f"My first reversed list of {mylist} is {reverse1}")

# Method 2
reverse2 = mylist[::-1]
print(f"My second reversed list of {mylist} is {reverse2}")

# Method 3
reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) - i -
                          1] = reverse3[len(reverse3) - i - 1], reverse3[i]
    # print(f"The reversed list at i={i} is {reverse3}")

print(f"My third reserved list of {mylist} is {reverse3}")

if reverse1 == reverse2 == reverse3:
    print("All the 3 methods give the same result.")

# PALLINDROMIFY THE LIST
# Given a list with some numbers.
# If the number is greater than 10 then print a list of next pallindrones. Otherwise print the number.

# Input:
    # [1, 6, 87, 43]

# Output:
    # [1, 6, 88, 44]

                    # SOLUTION

'''
Author: Jay Patil
Date: 8 August 2020
Purpose: Practice Problem
'''

def next_pallindrome(n):
    n = n+1
    while not is_pallindrome(n):
        n += 1

    return(n)


def is_pallindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    size = int(input("Enter the size of the list:\n"))
    numlist = []
    for i in range(size):
        numlist.append(int(input("Enter the number of the list:\n")))
    print(f"You have entered {numlist}")
 
# One Liner can also be done for the following code.
    new_list = []
    for element in numlist:
        if element >10:
            n = next_pallindrome(element)
            new_list.append(n)

        else:
            new_list.append(element)
    print(f"Your output list: {new_list}")

# ONE LINER FOR UPPER CODE
    # print(f"Your output list: {[numlist[i] if numlist[i]<10 else next_pallindrome(numlist[i]) for i in range(size)]}")


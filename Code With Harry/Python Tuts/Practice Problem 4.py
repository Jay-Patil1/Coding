# THE NEXT PALLINDROME
# A Pallindrome is a string which when reversed is equal to itself.
# Example: 616, mom, 676, 1000001
# Take an input from the user.
# Find the next pallindrome corrosponding to the given input.
# Input should be 'number of test cases' and then take all input from the user.

# Input:
    # Numbers

# Output:
    # Next pallindrome for 451 is 454

                    # SOLUTIONS

'''
Author: Jay Patil
Date: 7 August 2020
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

    n = int(input("Enter the number of test cases:\n"))
    numbers = []

    for i in range(n):
        number = int(input("Enter the number:\n"))
        numbers.append(number)
    print(numbers)

    for i in range(n):
        print(
            f"Next pallindrome for {numbers[i]} is {next_pallindrome(numbers[i])}")

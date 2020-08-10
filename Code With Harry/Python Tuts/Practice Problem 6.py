# GUESS THE NUMBER
# One has to guess a number between a and b.
# a and b are inputs from the user.
# Player 1 will have to keep choosing number and tell whether number is greater or smaller than the actual number.
# Log the number of trials it took to arrive to the number.
# Player 2 plays the same.
# Person with minimum guesses wins.

# Input:
    # a and b

# Output:
    # Player 1 (Guess)
    # Player 2 (Guess)

                    # SOLUTION

'''
Author: Jay Patil
Date: 8 August 2020
Purpose: Practice Problem
'''

import random

def guessGame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        
        if guess < actual:
            guess = int(input(f"Enter a bigger number:\n"))
            nguess += 1
        
        else:
            guess = int(input(f"Enter a smaller number:\n"))
            nguess += 1

    print(f"You guessed the number in {nguess} guesses!\n")
    return nguess
    

if __name__ == "__main__":
    print("Enter the range for the guess.")
    a = int(input("Enter the value of A:\n"))
    b = int(input("Enter the value of B:\n"))
    actual1 = random.randint(a, b)
    print("Player 1's Turn:\n")
    g1 = guessGame(a, b, actual1)
    print("Player 2's Turn:\n")
    actual2 = random.randint(a, b)
    g2 = guessGame(a, b, actual2)

    print(f"The number for Player 1 was {actual1}")
    print(f"The number for Player 2 was {actual2}\n")

    if g1 < g2:
        print("\t\t\t** Player 1 Wins! **\n")

    elif g1 > g2:
        print("\t\t\t** Player 2 Wins! **\n")

    else:
        print("\t\t\t\t** Its a Tie! **\n")

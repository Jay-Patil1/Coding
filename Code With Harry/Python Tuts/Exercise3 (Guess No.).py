# EXERCISE 3
# Take a input and continuously print till it is = N
# No of guesses 9
# Print No of guesses
# Game over if guess limit exceeds.

'''
Author: Jay Patil
Purpose: Learning Python
'''

                    # SOLUTION

N=18
No_of_guesses=1
print("You have 9 guesses")
while(No_of_guesses<10):
    inp = int(input("Guess the No."))
    if inp==N:
        print(" Congrats you guessed the No. Right!!")
        print("you took",No_of_guesses,"Guesses")
        break
    elif inp>N:
        print("The No.is less than your No.")
    elif inp<N:
        print("The No. is bigger than your No.")
    No_of_guesses = No_of_guesses + 1

if No_of_guesses>9:
    print("Game Over!")

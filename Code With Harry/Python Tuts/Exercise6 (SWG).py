# EXERCISE 6
# Game Development:Snake,Water,Gun
# Play game for 10 times.
# Announce the winner of every game.
# Announce the final winner.

                    #SOLUTION

'''
Author: Jay Patil
Purpose: Learning Python
'''

import random
lst = ["S","W","G"]

chance = 10
no_of_chance = 0
PointsH = 0
PointsC = 0

print("\t\t\t\t\tSnake,Water,Gun Game")
print("Select your choice\n"
      "S for Snake\n"
      "W for Water\n"
      "G for Gun\n")

while no_of_chance<chance :
    Hchoice = input("Snake,Water,Gun?\n")
    Cchoice = random.choice(lst)


    if Hchoice.upper() == Cchoice:
        print(f"You guessed {Hchoice} and Computer guessed {Cchoice}")
        print("Tie\n"
              "Both get 0 points.\n")
        no_of_chance = (no_of_chance + 1)
        print(f"{10 - no_of_chance} Chances Left.\n")

    elif Hchoice.upper()=="S" and Cchoice=="G":
        PointsC = PointsC + 1
        print(f"You guessed {Hchoice} and Computer guessed {Cchoice}" )
        print("You Loose.\t\t"
              "Computer gets 1 point.")
        print(f"You={PointsH} And Computer={PointsC}\n")
        no_of_chance = (no_of_chance + 1)
        print(f"{10 - no_of_chance} Chances Left.\n")

    elif Hchoice.upper()=="S" and Cchoice=="W":
        PointsH = PointsH + 1
        print(f"You guessed {Hchoice} and Computer guessed {Cchoice}" )
        print("You Win.\t\t"
              "You get 1 point.")
        print(f"You={PointsH} And Computer={PointsC}\n")
        no_of_chance = (no_of_chance + 1)
        print(f"{10 - no_of_chance} Chances Left.\n")

    elif Hchoice.upper()=="W" and Cchoice=="G":
        PointsH = PointsH + 1
        print(f"You guessed {Hchoice} and Computer guessed {Cchoice}")
        print("You Win\t\t"
              "You get 1 point.")
        print(f"You={PointsH} And Computer={PointsC}\n")
        no_of_chance = (no_of_chance + 1)
        print(f"{10 - no_of_chance} Chances Left.\n")


    elif Hchoice.upper()=="W" and Cchoice=="S":
        PointsC = PointsC + 1
        print(f"You guesses {Hchoice} and Computer guessed {Cchoice}")
        print("You loose.\t\t"
              "Computer gets 1 point.")
        print(f"You={PointsH} And Computer={PointsC}\n")
        no_of_chance = (no_of_chance + 1)
        print(f"{10 - no_of_chance} Chances Left.\n")

    elif Hchoice.upper()=="G" and Cchoice=="S":
        PointsH =PointsH + 1
        print(f"You guessed {Hchoice} and Computer guessed {Cchoice}")
        print("You Win.\t\t"
              "You get 1 point.")
        print(f"You={PointsH} And Computer={PointsC}\n")
        no_of_chance = (no_of_chance + 1)
        print(f"{10 - no_of_chance} Chances Left.\n")

    elif Hchoice.upper()=="G" and Cchoice=="W":
        PointsC = PointsC + 1
        print(f"You guessed {Hchoice} and Computer guessed {Cchoice}")
        print("You Loose.\t\t"
              "Computer gets 1 point.")
        print(f"You={PointsH} And Computer={PointsC}\n")
        no_of_chance = (no_of_chance + 1)
        print(f"{10 - no_of_chance} Chances Left.\n")


    else:
        print("Enter Valid Input.")
        no_of_chance = no_of_chance
        print(f"{10 - no_of_chance} Chances Left.\n")


print("\t\t\t\tGame Over\n")

if PointsC<PointsH:
    print("\t\t\t*Congrats You Win*")
elif PointsC>PointsH:
    print("\t\t\t   *You Loose*")
elif PointsC==PointsH:
    print("\t\t\t\t *Tie*")

print(f"Your Score = {PointsH} \t Ties = {10-(PointsH + PointsC)} \t Computer's Score = {PointsC}\n")

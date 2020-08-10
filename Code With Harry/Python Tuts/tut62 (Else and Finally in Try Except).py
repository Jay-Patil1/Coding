# ELSE AND FINALLY IN TRY EXCEPT.
f1 = open("HarryF.txt")

try:
    f = open("does2.txt")  # File doesnt exist.
    a = open("does.txt")

except IOError as e:  # If try fails then it goes to except else it is skipped. The error is printed. It is handled.
    print("IO error Occured.", e)
    # More than one except can be given.
except EOFError as e:
    print("EOF error Occured.", e)

# If except is run then else is not run and vice-versa.
else:
    print("This will run only if except is not running.")

finally:  # This is run anyway. If the exception occurs or not.
    # This is used to cleanup the code.
    print("Run this anyway.")
    # f.close()  # This file doesnt exist.
    f1.close()

print("important Stuff.")

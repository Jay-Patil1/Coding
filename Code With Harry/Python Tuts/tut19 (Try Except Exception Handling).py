# TRY EXCEPT EXCEPTION HANDLING
print("Enter num1")
num1 = input()
print("Enter num2")
num2 = input()
try:
    print("The sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important.")
# Try and except exception helps to give the error if any and continue the further program.
